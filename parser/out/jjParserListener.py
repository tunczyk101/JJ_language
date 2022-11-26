# Generated from jjParser.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
else:
    from jjParser import jjParser


# This class defines a complete listener for a parse tree produced by jjParser.
class jjParserListener(ParseTreeListener):
    functions_list = {}
    variables = {}
    statements = {}
    standard_func = {"println": []}

    # Enter a parse tree produced by jjParser#prog.
    def enterProg(self, ctx: jjParser.ProgContext):
        pass

    # Exit a parse tree produced by jjParser#prog.
    def exitProg(self, ctx: jjParser.ProgContext):
        print(self.functions_list)
        print(self.variables)
        pass

    # Enter a parse tree produced by jjParser#global_line.
    def enterGlobal_line(self, ctx: jjParser.Global_lineContext):
        pass

    # Exit a parse tree produced by jjParser#global_line.
    def exitGlobal_line(self, ctx: jjParser.Global_lineContext):
        pass

    # Enter a parse tree produced by jjParser#function.
    def enterFunction(self, ctx: jjParser.FunctionContext):
        print("FUNC " + str(ctx.NAME()))
        name = str(ctx.NAME())
        if self.functions_list.get(name) is None:
            self.functions_list.update({name: []})
            self.statements.update({ctx: []})
        else:
            print("UPDATE F")

    # Exit a parse tree produced by jjParser#function.
    def exitFunction(self, ctx: jjParser.FunctionContext):
        print("END FUNC  " + str(ctx.NAME()))
        print()
        print("$$$$$$$$$$$$$ CLEAR")
        self.variables.clear()
        pass

    # Enter a parse tree produced by jjParser#function_main.
    def enterFunction_main(self, ctx: jjParser.Function_mainContext):
        if self.functions_list.get("main") != None:
            print("!!!!!!!!!!!!!!!!!!! TYLKO JEDEN MAIN!!!")
            # exit(1)
        self.functions_list.update({"main": []})
        self.statements.update({ctx: []})
        # print(ctx.)
        pass

    # Exit a parse tree produced by jjParser#function_main.
    def exitFunction_main(self, ctx: jjParser.Function_mainContext):
        self.variables.clear()
        pass

    # Enter a parse tree produced by jjParser#optinal_function_blocks.
    def enterOptinal_function_blocks(self, ctx: jjParser.Optinal_function_blocksContext):
        pass

    # Exit a parse tree produced by jjParser#optinal_function_blocks.
    def exitOptinal_function_blocks(self, ctx: jjParser.Optinal_function_blocksContext):
        pass

    # Enter a parse tree produced by jjParser#argument_decl.
    def enterArgument_decl(self, ctx: jjParser.Argument_declContext):
        print("ENTER ARG DECL" + ctx.getText())
        name = str(ctx.NAME())
        if self.variables.get(name) is not None:
            raise Exception("VAR " + name + " ALREADY EXIST")
        self.variables.update({name: (ctx.MUTABLE_TOKEN() is not None)})
        pass

    # Exit a parse tree produced by jjParser#argument_decl.
    def exitArgument_decl(self, ctx: jjParser.Argument_declContext):
        print("END ARG DECL " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#additional_arguments_decl.
    def enterAdditional_arguments_decl(self, ctx: jjParser.Additional_arguments_declContext):
        print("ENTER ADD ARG " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#additional_arguments_decl.
    def exitAdditional_arguments_decl(self, ctx: jjParser.Additional_arguments_declContext):
        print("END ADD ARG " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#arguments_block.
    def enterArguments_block(self, ctx: jjParser.Arguments_blockContext):
        print("ARG BLOCK  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#arguments_block.
    def exitArguments_block(self, ctx: jjParser.Arguments_blockContext):
        print("END ARG BLOCK")
        pass

    # Enter a parse tree produced by jjParser#structural_block.
    def enterStructural_block(self, ctx: jjParser.Structural_blockContext):
        pass

    # Exit a parse tree produced by jjParser#structural_block.
    def exitStructural_block(self, ctx: jjParser.Structural_blockContext):
        pass

    # Enter a parse tree produced by jjParser#return_block.
    def enterReturn_block(self, ctx: jjParser.Return_blockContext):
        print("ENTER RETURN  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#return_block.
    def exitReturn_block(self, ctx: jjParser.Return_blockContext):
        print("END RETURN  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#guard_block.
    def enterGuard_block(self, ctx: jjParser.Guard_blockContext):
        print("ENTER GUARD  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#guard_block.
    def exitGuard_block(self, ctx: jjParser.Guard_blockContext):
        print("END GUARD  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#structural_line.
    def enterStructural_line(self, ctx: jjParser.Structural_lineContext):
        pass

    # Exit a parse tree produced by jjParser#structural_line.
    def exitStructural_line(self, ctx: jjParser.Structural_lineContext):
        pass

    # Enter a parse tree produced by jjParser#variable_declaration.
    def enterVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        print("ENTER VAR DEC  " + ctx.getText())
        # print(ctx.MUTABLE_TOKEN())
        name = str(ctx.NAME())
        if self.variables.get(name) != None:
            print("!!!!! PONOWNA DEKLARACJA ZMIENNEJ: " + name)
            # exit(1)
        self.variables.update({name: (ctx.MUTABLE_TOKEN() is not None)})
        self.statements[list(self.statements.keys())[-1]].append(name)
        pass

    # Exit a parse tree produced by jjParser#variable_declaration.
    def exitVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        print("END VAR DEC  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#instruction_line.
    def enterInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        pass

    # Exit a parse tree produced by jjParser#instruction_line.
    def exitInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        pass

    # Enter a parse tree produced by jjParser#structural_line_instruction.
    def enterStructural_line_instruction(self, ctx: jjParser.Structural_line_instructionContext):
        pass

    # Exit a parse tree produced by jjParser#structural_line_instruction.
    def exitStructural_line_instruction(self, ctx: jjParser.Structural_line_instructionContext):
        pass

    # Enter a parse tree produced by jjParser#statement.
    def enterStatement(self, ctx: jjParser.StatementContext):
        pass

    # Exit a parse tree produced by jjParser#statement.
    def exitStatement(self, ctx: jjParser.StatementContext):
        pass

    # Enter a parse tree produced by jjParser#instruction.
    def enterInstruction(self, ctx: jjParser.InstructionContext):
        print("ENTER INSTRUCTION  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#instruction.
    def exitInstruction(self, ctx: jjParser.InstructionContext):
        pass

    # Enter a parse tree produced by jjParser#expresion_in_parenthesis.
    def enterExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        pass

    # Exit a parse tree produced by jjParser#expresion_in_parenthesis.
    def exitExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        print("END EXP IN PARENT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#left_of_binary_operation.
    def enterLeft_of_binary_operation(self, ctx: jjParser.Left_of_binary_operationContext):
        print("ENTER BIN OP  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#left_of_binary_operation.
    def exitLeft_of_binary_operation(self, ctx: jjParser.Left_of_binary_operationContext):
        print("END BIN OP  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#all_binary_operations.
    def enterAll_binary_operations(self, ctx: jjParser.All_binary_operationsContext):
        print("ENTER ALL BIN OP  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#all_binary_operations.
    def exitAll_binary_operations(self, ctx: jjParser.All_binary_operationsContext):
        print("END ALL BIN OP  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#all_unary_operations.
    def enterAll_unary_operations(self, ctx: jjParser.All_unary_operationsContext):
        print("ENTER ALL UNARY OP  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#all_unary_operations.
    def exitAll_unary_operations(self, ctx: jjParser.All_unary_operationsContext):
        print("END ALL UNARY OP  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#expresion.
    def enterExpresion(self, ctx: jjParser.ExpresionContext):
        print("ENTER EX  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#expresion.
    def exitExpresion(self, ctx: jjParser.ExpresionContext):
        print("END EX  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#function_call.
    def enterFunction_call(self, ctx: jjParser.Function_callContext):
        print("ENTER FUNC CALL  " + ctx.getText())
        name = str(ctx.NAME())
        if self.functions_list.get(name) is None and self.standard_func.get(name) is None:
            raise Exception("NIE ZADEKLROWANO FUNC: " + name)
        pass

    # Exit a parse tree produced by jjParser#function_call.
    def exitFunction_call(self, ctx: jjParser.Function_callContext):
        print("END FUNC CALL  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#identifier.
    def enterIdentifier(self, ctx: jjParser.IdentifierContext):
        pass

    # Exit a parse tree produced by jjParser#identifier.
    def exitIdentifier(self, ctx: jjParser.IdentifierContext):
        pass

    # Enter a parse tree produced by jjParser#value.
    def enterValue(self, ctx: jjParser.ValueContext):
        print("ENTER VAL  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#value.
    def exitValue(self, ctx: jjParser.ValueContext):
        print("END VAL  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#if_statement_start.
    def enterIf_statement_start(self, ctx: jjParser.If_statement_startContext):
        print("ENTER STAT START  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#if_statement_start.
    def exitIf_statement_start(self, ctx: jjParser.If_statement_startContext):
        print("END STAT START  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#if_statement.
    def enterIf_statement(self, ctx: jjParser.If_statementContext):
        self.statements.update({ctx: []})
        pass

    # Exit a parse tree produced by jjParser#if_statement.
    def exitIf_statement(self, ctx: jjParser.If_statementContext):
        for v in self.statements[ctx]:
            self.variables.pop(v)
        self.statements.pop(ctx)
        pass

    # Enter a parse tree produced by jjParser#else_statement.
    def enterElse_statement(self, ctx: jjParser.Else_statementContext):
        self.statements.update({ctx: []})
        pass

    # Exit a parse tree produced by jjParser#else_statement.
    def exitElse_statement(self, ctx: jjParser.Else_statementContext):
        for v in self.statements[ctx]:
            self.variables.pop(v)
        self.statements.pop(ctx)
        pass

    # Enter a parse tree produced by jjParser#while_statement.
    def enterWhile_statement(self, ctx: jjParser.While_statementContext):
        self.statements.update({ctx: []})
        pass

    # Exit a parse tree produced by jjParser#while_statement.
    def exitWhile_statement(self, ctx: jjParser.While_statementContext):
        for v in self.statements[ctx]:
            self.variables.pop(v)
        self.statements.pop(ctx)
        pass

    # Enter a parse tree produced by jjParser#for_statement.
    def enterFor_statement(self, ctx: jjParser.For_statementContext):
        self.statements.update({ctx: []})
        pass

    # Exit a parse tree produced by jjParser#for_statement.
    def exitFor_statement(self, ctx: jjParser.For_statementContext):
        for v in self.statements[ctx]:
            self.variables.pop(v)
        self.statements.pop(ctx)
        pass

    # Enter a parse tree produced by jjParser#assignmnet_statement.
    def enterAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        print("ENTER ASSIG STAT  " + ctx.getText())

        name = str(ctx.NAME())

        if self.variables.get(name) is None:
            raise Exception("NIE ZADEKLAROWANO ZMIENNEJ: " + name)

        elif not self.variables.get(name):
            # print("!!!!!!!!!!!!!!! ZMIENNA NIE JEST ZMIENNA")
            raise Exception("ZMIENNA: " + name + " NIE JEST ZMIENNA")

    # Exit a parse tree produced by jjParser#assignmnet_statement.
    def exitAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        print("END ASSIG STAT  " + ctx.getText())
        pass

    def run(self, node):
        print("run")
        self.vars = {}
        self.stack = []
        self.functions = {}
        ParseTreeWalker().walk(self, node)


del jjParser
