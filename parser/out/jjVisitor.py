from antlr4 import *

if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
    from .jjParserVisitor import jjParserVisitor
    from .logger import Logger
else:
    from jjParser import jjParser
    from jjParserVisitor import jjParserVisitor
    from logger import Logger


class UnaryOperations:
    def negate(value): return not value
    def minus(value): return -value
    def plus(value): return value

class BinaryOperations:
    def add(left, right): return left + right
    def sub(left, right): return left - right
    def mul(left, right): return left * right
    def div(left, right): return left / right
    def mod(left, right): return left % right
    def eq(left, right): return left == right
    def not_eq(left, right): return left != right
    def less(left, right): return left < right
    def more(left, right): return left > right
    def less_eq(left, right): return left >= right
    def more_eq(left, right): return left <= right
    def or_fn(left, right): return left or right
    def and_fn(left, right): return left and right

class jjVisitor(jjParserVisitor):


    def __init__(self, verbose = False):
        super().__init__()
        self.logger = Logger(verbose)

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
        return self.visitExpresion(ctx.getChild(0, jjParser.ExpresionContext))

    def visitExpresion(self, ctx: jjParser.ExpresionContext):
        if ctx.getChildCount() == 3:
            left = self.visitLeft_of_binary_operation(ctx.getChild(0, jjParser.Left_of_binary_operationContext))
            bin_op_fn = self.visitAll_binary_operations(ctx.getChild(0, jjParser.All_binary_operationsContext))
            right = self.visitExpresion(ctx.getChild(0, jjParser.ExpresionContext))
            return bin_op_fn(left, right)
        
        unary = ctx.getChild(0, jjParser.All_unary_operationsContext)
        if unary is not None:
            return self.visitAll_unary_operations(unary)(self.visitExpresion(ctx.getChild(0, jjParser.ExpresionContext)))

        return super().visitExpresion(ctx)

    def visitChildren(self, node):
        value = super().visitChildren(node)
        self.logger.log("visited: " + node.getText() + " -> " + str(value))
        return value
    
