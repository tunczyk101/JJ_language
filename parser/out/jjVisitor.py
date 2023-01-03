import collections
from antlr4 import *

from typing import Any, Optional
from dataclasses import dataclass

if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
    from .jjParserVisitor import jjParserVisitor
    from .logger import Logger
    from .operations import UnaryOperations, BinaryOperations
    from .ast import AST
else:
    from jjParser import jjParser
    from jjParserVisitor import jjParserVisitor
    from logger import Logger
    from operations import UnaryOperations, BinaryOperations
    from ast import AST

@dataclass
class Variable:
    is_mutable: bool
    name: str
    value: Any

@dataclass
class Function_Argument:
    name: str
    is_mutable: bool

    @staticmethod
    def from_argument_decl(argument_decl: jjParser.Argument_declContext) -> 'Function_Argument':
        return Function_Argument(argument_decl.NAME(), argument_decl.MUTABLE() is not None)

    @staticmethod
    def parse_all(argument_block: jjParser.Arguments_blockContext) -> list['Function_Argument']:
        arguments = []
        
        if(argument_block is None):
            return arguments
        
        arguments.append(Function_Argument.from_argument_decl(argument_block.argument_decl()))
        for additional_argument in argument_block.additional_arguments_decl():
            arguments.append(Function_Argument.from_argument_decl(additional_argument.argument_decl()))
        return arguments

@dataclass
class Function_specialization:
    guard: Optional[jjParser.ExpresionContext]
    body_block: Optional[jjParser.Structural_blockContext]
    return_block: Optional[jjParser.Return_blockContext]

    @staticmethod
    def from_optional_function_blocks(optional_function_blocks: jjParser.Optinal_function_blocksContext) -> 'Function_specialization':
        return Function_specialization(optional_function_blocks.guard_block(), optional_function_blocks.structural_block(), optional_function_blocks.return_block())

@dataclass
class Function:
    name: str
    arguments: list[str]
    specializations: list[Function_specialization]

    @staticmethod
    def from_function_context(function_context: jjParser.FunctionContext) -> 'Function':
        name = str(function_context.NAME())
        arguments = Function_Argument.parse_all(function_context.optinal_function_blocks().arguments_block())
        specialisation = Function_specialization.from_optional_function_blocks(function_context.optinal_function_blocks())
        
        return Function(name, arguments, [specialisation])
     
class STD_functions:
    def println(args): print(' '.join(map(lambda x: str(x), args)))

class jjVisitor(jjParserVisitor):

    def __init__(self):
        super().__init__()
        self.variablesStack = collections.deque()
        self.functions = {}

    def addFunction(self, ctx: jjParser.FunctionContext):
        func = Function.from_function_context(ctx)
        
        if func.name in self.functions:
            # todo
            pass
        else:
            self.functions.update({func.name:func})
            print(f"Added function '{func.name}'")
        

    def getVariable(self, name):
        for var in reversed(self.variablesStack):
            if var is not None and var.name == name:
                return var

        print(f"ERROR: variable '{name}' is not defined.")
        exit(0)

    def getVariableValue(self, name):
        return self.getVariable(name).value

    def setVariableValue(self, name, value):
        self.getVariable(name).value = value

    def stack_start_block(self):
        self.variablesStack.append(None)

    def stack_end_block(self):
        while(self.variablesStack[-1] is not None):
            self.variablesStack.pop()
        self.variablesStack.pop()

    def get_std_fn(self, name):
        match name:
            case "println": return STD_functions.println
        
    def visitStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.stack_start_block()
        super().visitStructural_block(ctx)
        self.stack_end_block()

    def visitVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        self.variablesStack.append(Variable(
            is_mutable = ctx.MUTABLE_TOKEN() is not None, 
            name = str(ctx.NAME()),
            value = self.visitExpresion(ctx.expresion()).get_value()
        ))
        
    def visitFunction_call(self, ctx: jjParser.Function_callContext):   
        std_fn = self.get_std_fn(str(ctx.NAME()))
        if(std_fn is not None):
            std_fn([self.visitExpresion(child).get_value() for child in ctx.children if isinstance(child, jjParser.ExpresionContext)])

        return super().visitFunction_call(ctx)

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
             case '!': return UnaryOperations.negate
             case '-': return UnaryOperations.minus
             case '+': return UnaryOperations.plus

    def visitAll_binary_operations(self, ctx: jjParser.All_binary_operationsContext):
        text = ctx.getText()
        match text:
            case '*': return (BinaryOperations.mul, 6)
            case '/': return (BinaryOperations.div, 6)
            case '%': return (BinaryOperations.mod, 6)
            case '==': return (BinaryOperations.eq, 3)
            case '!=': return (BinaryOperations.not_eq, 3)
            case '<': return (BinaryOperations.less, 4)
            case '>': return (BinaryOperations.more, 4)
            case '<=': return (BinaryOperations.less_eq, 4)
            case '>=': return (BinaryOperations.more_eq, 4)
            case '||': return (BinaryOperations.or_fn, 1)
            case '&&': return (BinaryOperations.and_fn, 2)
            case '+': return (BinaryOperations.add, 5)
            case '-': return (BinaryOperations.sub, 5)

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
            return self.getVariableValue(str(name))

        return self.visitValue(ctx.value())

    def visitAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        value = self.visitExpresion(ctx.expresion()).get_value()
        name = str(ctx.NAME())

        if(type(self.getVariableValue(name)) != type(value)):
            print(f"ERROR: Variable '{name}' is not of type {type(value)}")
            exit(1)

        self.setVariableValue(name, value)

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

        if (isinstance(value, AST)):
            value = value.get_value()

        type_name = str(ctx.TYPE_NAME())

        token_name = lambda x: jjParser.literalNames[x].removeprefix("'").removesuffix("'")

        if type_name == token_name(jjParser.INT_TYPE):
            return int(value)
        if type_name == token_name(jjParser.FLOAT_TYPE):
            return float(value)
        if type_name == token_name(jjParser.BOOL_TYPE):
            return bool(value)
        
        print("INTERNAL ERROR!")
        exit(1)

    def visitFunction(self, ctx: jjParser.FunctionContext):
        self.addFunction(ctx)
