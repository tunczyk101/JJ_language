# Generated from jjParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
else:
    from jjParser import jjParser

# This class defines a complete generic visitor for a parse tree produced by jjParser.

class jjParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jjParser#prog.
    def visitProg(self, ctx:jjParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#global_line.
    def visitGlobal_line(self, ctx:jjParser.Global_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#function.
    def visitFunction(self, ctx:jjParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#function_main.
    def visitFunction_main(self, ctx:jjParser.Function_mainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#optinal_function_blocks.
    def visitOptinal_function_blocks(self, ctx:jjParser.Optinal_function_blocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#argument_decl.
    def visitArgument_decl(self, ctx:jjParser.Argument_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#additional_arguments_decl.
    def visitAdditional_arguments_decl(self, ctx:jjParser.Additional_arguments_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#arguments_block.
    def visitArguments_block(self, ctx:jjParser.Arguments_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#structural_block.
    def visitStructural_block(self, ctx:jjParser.Structural_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#return_block.
    def visitReturn_block(self, ctx:jjParser.Return_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#guard_block.
    def visitGuard_block(self, ctx:jjParser.Guard_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#structural_line.
    def visitStructural_line(self, ctx:jjParser.Structural_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#variable_declaration.
    def visitVariable_declaration(self, ctx:jjParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#instruction_line.
    def visitInstruction_line(self, ctx:jjParser.Instruction_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#structural_line_instruction.
    def visitStructural_line_instruction(self, ctx:jjParser.Structural_line_instructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#statement.
    def visitStatement(self, ctx:jjParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#instruction.
    def visitInstruction(self, ctx:jjParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#expresion_in_parenthesis.
    def visitExpresion_in_parenthesis(self, ctx:jjParser.Expresion_in_parenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#left_of_binary_operation.
    def visitLeft_of_binary_operation(self, ctx:jjParser.Left_of_binary_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#all_binary_operations.
    def visitAll_binary_operations(self, ctx:jjParser.All_binary_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#all_unary_operations.
    def visitAll_unary_operations(self, ctx:jjParser.All_unary_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#expresion.
    def visitExpresion(self, ctx:jjParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#function_call.
    def visitFunction_call(self, ctx:jjParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#identifier.
    def visitIdentifier(self, ctx:jjParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#value.
    def visitValue(self, ctx:jjParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#if_statement_start.
    def visitIf_statement_start(self, ctx:jjParser.If_statement_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#if_statement.
    def visitIf_statement(self, ctx:jjParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#else_statement.
    def visitElse_statement(self, ctx:jjParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#while_statement.
    def visitWhile_statement(self, ctx:jjParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#for_statement.
    def visitFor_statement(self, ctx:jjParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jjParser#assignmnet_statement.
    def visitAssignmnet_statement(self, ctx:jjParser.Assignmnet_statementContext):
        return self.visitChildren(ctx)



del jjParser