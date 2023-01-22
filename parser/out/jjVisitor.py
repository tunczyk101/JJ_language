import collections

from typing import Any
from dataclasses import dataclass

if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
    from .jjParserVisitor import jjParserVisitor
    from .jjErrorListener import print_semantic_error
    from .operations import UnaryOperations, BinaryOperations
    from .ast import AST
    from .functions import Function, STANDARD_FUNCTIONS, VariadicArguments
else:
    from jjParser import jjParser
    from jjParserVisitor import jjParserVisitor
    from jjErrorListener import print_semantic_error
    from operations import UnaryOperations, BinaryOperations
    from ast import AST
    from functions import Function, STANDARD_FUNCTIONS, VariadicArguments


@dataclass
class Variable:
    is_mutable: bool
    name: str
    value: Any


class jjVisitor(jjParserVisitor):

    def __init__(self):
        super().__init__()
        self.variablesStack = collections.deque()
        self.functions = {}
        self.FUNCTIONS_STACK_SIZE = 40
        self.functions_stack_counter = 0

    def addFunction(self, ctx: jjParser.FunctionContext):
        func = Function.from_function_context(ctx)

        if func.name in self.functions:
            parent = self.functions[func.name]

            if len(func.arguments) != len(parent.arguments):
                print_semantic_error(f"function '{func.name}' already defined with different number of arguments ({len(parent.arguments)}).")
                exit(0)

            if func.specializations[0].guard_block is None:
                print_semantic_error(f"function '{func.name}' already defined.")
                exit(0)

            if not ((func.specializations[0].return_block is None and parent.specializations[0].return_block is None)
                or (func.specializations[0].return_block is not None and parent.specializations[0].return_block is not None)):
                print_semantic_error(f"function '{func.name}' already defined with different return type.")
                exit(0)

            self.functions[func.name].specializations.append(func.specializations[0])
        else:
            self.functions.update({func.name: func})

    def get_current_func_specializations(self, func: Function):
        for specialization in reversed(func.specializations):
            if specialization.guard_block is None or self.visitExpresion(
                    specialization.guard_block.expresion()).get_value():
                return specialization

    def getVariable(self, name, ctx, scope=0):
        for var in reversed(self.variablesStack):
            if var is None and scope > 0:
                scope -= 1
                continue
            if scope == 0 and var is not None and var.name == name:
                return var

        print_semantic_error(f"variable '{name}' is not defined.", ctx.start.line, ctx.start.column)
        exit(0)

    def getVariableValue(self, name, ctx, scope=0):
        return self.getVariable(name, ctx, scope).value

    def setVariableValue(self, name, value, ctx, scope=0):
        self.getVariable(name, ctx, scope).value = value

    def stack_start_block(self):
        self.variablesStack.append(None)

    def stack_end_block(self):
        while self.variablesStack[-1] is not None:
            self.variablesStack.pop()
        self.variablesStack.pop()

    def get_std_fn(self, name):
        if name in STANDARD_FUNCTIONS:
            return STANDARD_FUNCTIONS[name]

    def visitStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.stack_start_block()
        super().visitStructural_block(ctx)
        self.stack_end_block()

    def visitVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        name = str(ctx.NAME())
        expr_ctx = ctx.expresion()
        value = self.visitExpresion(expr_ctx).get_value()

        if expr_ctx.function_call() is not None and value is None:
            print_semantic_error(
                f"variable '{name}' can't be initialized with function '{expr_ctx.function_call().NAME()}' "
                f"that is not returning a value.", ctx.start.line, ctx.start.column)

        self.variablesStack.append(Variable(
            is_mutable=ctx.MUTABLE_TOKEN() is not None,
            name=name,
            value=value
        ))

    def visitFunction_call(self, ctx: jjParser.Function_callContext):
        def error_bad_arg_count(func_name, expected, given):
            print_semantic_error(f"function '{func_name}' expected {expected} arguments, but {given} were given.",
                                 ctx.start.line, ctx.start.column)
            exit(0)

        self.functions_stack_counter += 1
        if self.functions_stack_counter > self.FUNCTIONS_STACK_SIZE:
            print(f"Runtime Error: Function call stack overflow.")
            exit(0)

        fn_name = str(ctx.NAME())
        std_fn = self.get_std_fn(fn_name)
        arguments_ctx = [child for child in ctx.children if isinstance(child, jjParser.ExpresionContext)]
        arguments = [self.visitExpresion(child).get_value() for child in arguments_ctx]
        variable_args_names = [str(child.identifier().NAME()) if child.identifier() is not None else None for child in
                               arguments_ctx]

        result = None

        if std_fn is not None:
            if isinstance(std_fn.arguments_count, VariadicArguments) or len(arguments) == std_fn.arguments_count:
                std_fn.call(arguments, ctx)
            else:
                error_bad_arg_count(fn_name, std_fn.arguments_count, len(arguments))
        elif fn_name in self.functions:
            self.stack_start_block()
            func = self.functions[fn_name]

            if len(func.arguments) > 0:
                if len(arguments) == len(func.arguments):
                    for i in range(len(arguments)):
                        if func.arguments[i].is_mutable and variable_args_names[i] is None:
                            print_semantic_error(f"can't pass expression as mutable argument to function '{fn_name}'.",
                                                 ctx.start.line, ctx.start.column)
                            exit(1)

                        self.variablesStack.append(Variable(
                            is_mutable=func.arguments[i].is_mutable,
                            name=func.arguments[i].name,
                            value=arguments[i]
                        ))
                else:
                    error_bad_arg_count(fn_name, len(func.arguments), len(arguments))

            func_specializations = self.get_current_func_specializations(func)
            func_struct_block = func_specializations.body_block
            func_return_block = func_specializations.return_block

            if func_struct_block is not None:
                self.visitStructural_block(func_struct_block)

            if func_return_block is not None:
                result = self.visitExpresion(func_return_block.expresion())

            for i, arg in enumerate(func.arguments):
                if arg.is_mutable:
                    self.setVariableValue(variable_args_names[i], self.getVariableValue(arg.name, ctx), ctx, 1),

            self.stack_end_block()

        self.functions_stack_counter -= 1

        return result

    def visitValue(self, ctx: jjParser.ValueContext):
        bool_val = ctx.BOOL()
        if bool_val is not None:
            return str(bool_val) == 'true'
        else:
            num_str = str(ctx.NUMBER_TYPE())
            return float(num_str) if '.' in num_str else int(num_str)

    def visitAll_unary_operations(self, ctx: jjParser.All_unary_operationsContext):
        text = ctx.getText()
        match text:
            case '!':
                return UnaryOperations.negate
            case '-':
                return UnaryOperations.minus
            case '+':
                return UnaryOperations.plus

    def visitAll_binary_operations(self, ctx: jjParser.All_binary_operationsContext):
        text = ctx.getText()
        match text:
            case '*':
                return BinaryOperations.mul, 6
            case '/':
                return BinaryOperations.div, 6
            case '%':
                return BinaryOperations.mod, 6
            case '==':
                return BinaryOperations.eq, 3
            case '!=':
                return BinaryOperations.not_eq, 3
            case '<':
                return BinaryOperations.less, 4
            case '>':
                return BinaryOperations.more, 4
            case '<=':
                return BinaryOperations.less_eq, 4
            case '>=':
                return BinaryOperations.more_eq, 4
            case '||':
                return BinaryOperations.or_fn, 1
            case '&&':
                return BinaryOperations.and_fn, 2
            case '+':
                return BinaryOperations.add, 5
            case '-':
                return BinaryOperations.sub, 5

    def visitExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        return AST(self.visitExpresion(ctx.expresion()))

    def visitExpresion(self, ctx: jjParser.ExpresionContext):
        if ctx.getChildCount() == 3:
            left = self.visitLeft_of_binary_operation(ctx.left_of_binary_operation())
            bin_op, prority = self.visitAll_binary_operations(ctx.all_binary_operations())
            right = self.visitExpresion(ctx.expresion())

            return AST(left, (bin_op, prority, right))

        unary = ctx.all_unary_operations()
        if unary is not None:
            value = self.visitExpresion(ctx.expresion()).get_value()
            value_after_op = type(value)(self.visitAll_unary_operations(unary)(value))
            return AST(value_after_op)

        return AST(super().visitExpresion(ctx))

    def visitIf_statement_start(self, ctx: jjParser.If_statement_startContext):
        return self.visitExpresion_in_parenthesis(ctx.expresion_in_parenthesis()).get_value()

    def visitIf_statement(self, ctx: jjParser.If_statementContext):
        if self.visitIf_statement_start(ctx.if_statement_start()):
            self.visitStructural_block(ctx.structural_block())
        else:
            else_stm = ctx.else_statement()
            if else_stm is not None:
                self.visitElse_statement(else_stm)

    def visitElse_statement(self, ctx: jjParser.Else_statementContext):
        if_smt = ctx.if_statement()
        if if_smt is not None:
            self.visitIf_statement(if_smt)
        else:
            self.visitStructural_block(ctx.structural_block())

    def visitChildren(self, node):
        value = super().visitChildren(node)
        return value

    def visitIdentifier(self, ctx: jjParser.IdentifierContext):
        name = ctx.NAME()
        if name is not None:
            return self.getVariableValue(str(name), ctx, 1 if ctx.SCOPE_PARENT_TOKEN() is not None else 0)

        return self.visitValue(ctx.value())

    def visitAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        expr_ctx = ctx.expresion()
        value = self.visitExpresion(ctx.expresion()).get_value()
        name = str(ctx.NAME())

        if expr_ctx.function_call() is not None and value is None:
            print_semantic_error(
                f"Can't assign function '{expr_ctx.function_call().NAME()}' that returns nothing to variable '{name}'.",
                ctx.start.line, ctx.start.column)
            exit(1)

        if type(self.getVariableValue(name, ctx)) != type(value):
            print_semantic_error(f"Variable '{name}' is not of type {type(value)}.", ctx.start.line, ctx.start.column)
            exit(1)

        self.setVariableValue(name, value, ctx, 1 if ctx.SCOPE_PARENT_TOKEN() is not None else 0)

    def visitInstruction(self, ctx: jjParser.InstructionContext):
        expr = ctx.expresion()
        if expr is not None:
            return self.visitExpresion(expr).get_value()
        return super().visitInstruction(ctx)

    def visitInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        intruction = ctx.instruction()
        if intruction is not None:
            return self.visitInstruction(intruction)
        return None

    def visitFor_statement(self, ctx: jjParser.For_statementContext):
        self.stack_start_block()

        self.visitInstruction_line(ctx.instruction_line(0))
        while self.visitInstruction_line(ctx.instruction_line(1)):
            self.visitStructural_block(ctx.structural_block())
            self.visitInstruction(ctx.instruction())

        self.stack_end_block()

    def visitWhile_statement(self, ctx: jjParser.While_statementContext):
        self.stack_start_block()

        while self.visitExpresion_in_parenthesis(ctx.expresion_in_parenthesis()).get_value():
            self.visitStructural_block(ctx.structural_block())

        self.stack_end_block()

    def visitCast_expression(self, ctx: jjParser.Cast_expressionContext):
        value = self.visitLeft_of_cast_expr(ctx.left_of_cast_expr())

        if isinstance(value, AST):
            value = value.get_value()

        type_name = str(ctx.TYPE_NAME())

        token_name = lambda x: jjParser.literalNames[x].removeprefix("'").removesuffix("'")

        if type_name == token_name(jjParser.INT_TYPE):
            return int(value)
        if type_name == token_name(jjParser.FLOAT_TYPE):
            return float(value)
        if type_name == token_name(jjParser.BOOL_TYPE):
            return bool(value)

        print_semantic_error("INTERNAL ERROR!", ctx.start.line, ctx.start.column)
        exit(1)

    def visitFunction(self, ctx: jjParser.FunctionContext):
        self.addFunction(ctx)
