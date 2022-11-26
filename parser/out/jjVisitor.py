import collections
from antlr4 import *

from typing import Any
from dataclasses import dataclass

if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
    from .jjParserVisitor import jjParserVisitor
    from .logger import Logger
    from .operations import UnaryOperations, BinaryOperations
else:
    from jjParser import jjParser
    from jjParserVisitor import jjParserVisitor
    from logger import Logger

@dataclass
class Variable:
    isMutable: bool
    name: str
    value: Any 

class jjVisitor(jjParserVisitor):

    def __init__(self):
        super().__init__()
        self.variablesStack = collections.deque()

    def getVariableValue(self, name):
        for var in self.variablesStack:
            if var is not None and var.name == name:
                return var.value

        print(f"ERROR: variable '{name}' is not defined.")
        exit(0)

    def visitStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.variablesStack.append(None)

        super().visitStructural_block(ctx)
        
        while(self.variablesStack[-1] is not None):
            self.variablesStack.pop()
        self.variablesStack.pop()

    def visitVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        self.variablesStack.append(Variable(
            isMutable = ctx.MUTABLE_TOKEN() is not None, 
            name = str(ctx.NAME()),
            value = self.visitExpresion(ctx.expresion())
        ))
        
    def visitValue(self, ctx: jjParser.ValueContext):
        bool = ctx.BOOL()
        if bool is not None:
            return str(bool) == 'true'
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
            case '*': return BinaryOperations.mul
            case '/': return BinaryOperations.div
            case '%': return BinaryOperations.mod
            case '==': return BinaryOperations.eq
            case '!=': return BinaryOperations.not_eq
            case '<': return BinaryOperations.less
            case '>': return BinaryOperations.more
            case '<=': return BinaryOperations.less_eq
            case '>=': return BinaryOperations.more_eq
            case '||': return BinaryOperations.or_fn
            case '&&': return BinaryOperations.and_fn
            case '+': return BinaryOperations.add
            case '-': return BinaryOperations.sub

    def visitExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        return self.visitExpresion(ctx.expresion())

    def visitExpresion(self, ctx: jjParser.ExpresionContext):
        if ctx.getChildCount() == 3:
            left = self.visitLeft_of_binary_operation(ctx.left_of_binary_operation())
            bin_op_fn = self.visitAll_binary_operations(ctx.all_binary_operations())
            right = self.visitExpresion(ctx.expresion())
            return bin_op_fn(left, right)
        
        unary = ctx.all_unary_operations()
        if unary is not None:
            return self.visitAll_unary_operations(unary)(self.visitExpresion(ctx.expresion()))

        return super().visitExpresion(ctx)

    def visitChildren(self, node):
        value = super().visitChildren(node)
        return value

    def visitIdentifier(self, ctx: jjParser.IdentifierContext):
        name = ctx.NAME()
        if(name is not None):
            return self.getVariableValue(str(name))

        return self.visitValue(ctx.value())
    
