import collections
from antlr4 import *

from typing import Any
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

class STD_functions:
    def println(args): print(' '.join(map(lambda x: str(x), args)))

class jjVisitor(jjParserVisitor):

    def __init__(self):
        super().__init__()
        self.variablesStack = collections.deque()

    def getVariableValue(self, name):
        for var in reversed(self.variablesStack):
            if var is not None and var.name == name:
                return var.value

        print(f"ERROR: variable '{name}' is not defined.")
        exit(0)

    def get_std_fn(self, name):
        match name:
            case "println": return STD_functions.println
        
    def visitStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.variablesStack.append(None)

        super().visitStructural_block(ctx)
        
        while(self.variablesStack[-1] is not None):
            self.variablesStack.pop()
        self.variablesStack.pop()

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
            return AST(self.visitAll_unary_operations(unary)(self.visitExpresion(ctx.expresion()).get_value()))

        return AST(super().visitExpresion(ctx))

    def visitIf_statement_start(self, ctx: jjParser.If_statement_startContext):
        return self.visitExpresion_in_parenthesis(ctx.expresion_in_parenthesis())

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
    
