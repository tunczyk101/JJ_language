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

    # Enter a parse tree produced by jjParser#prog.
    def enterProg(self, ctx: jjParser.ProgContext):
        print("Enter prog")
        pass

    # Exit a parse tree produced by jjParser#prog.
    def exitProg(self, ctx: jjParser.ProgContext):
        print("Exit prog")
        print(self.functions_list)
        print(self.variables)
        pass

    # Enter a parse tree produced by jjParser#global_line.
    def enterGlobal_line(self, ctx: jjParser.Global_lineContext):
        print("Global line")
        pass

    # Exit a parse tree produced by jjParser#global_line.
    def exitGlobal_line(self, ctx: jjParser.Global_lineContext):
        print("out of global line")
        pass

    # Enter a parse tree produced by jjParser#function.
    def enterFunction(self, ctx: jjParser.FunctionContext):
        print("FUNC " + str(ctx.NAME()))
        name = str(ctx.NAME())
        if self.functions_list.get(name) is None:
            self.functions_list.update({name: []})
        else:
            print("UPDATE F")

    # Exit a parse tree produced by jjParser#function.
    def exitFunction(self, ctx: jjParser.FunctionContext):
        print("END FUNC  " + str(ctx.NAME()))
        print()
        print(self.variables)
        print()
        print("$$$$$$$$$$$$$ CLEAR")
        self.vars.clear()
        pass

    # Enter a parse tree produced by jjParser#function_main.
    def enterFunction_main(self, ctx: jjParser.Function_mainContext):
        print("MAIN  " + ctx.getText())
        # print(self.functions_list.get("main"))
        if self.functions_list.get("main") != None:
            print("!!!!!!!!!!!!!!!!!!! TYLKO JEDEN MAIN!!!")
            # exit(1)
        self.functions_list.update({"main": []})
        # print(ctx.)
        pass

    # Exit a parse tree produced by jjParser#function_main.
    def exitFunction_main(self, ctx: jjParser.Function_mainContext):
        print("OUT MAIN")
        self.variables.clear()
        pass

    # Enter a parse tree produced by jjParser#optinal_function_blocks.
    def enterOptinal_function_blocks(self, ctx: jjParser.Optinal_function_blocksContext):
        print("OPTIONAL FUNC BLOCKS  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#optinal_function_blocks.
    def exitOptinal_function_blocks(self, ctx: jjParser.Optinal_function_blocksContext):
        print("END OPTIONAL FUNC BLOCKS  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#argument_decl.
    def enterArgument_decl(self, ctx: jjParser.Argument_declContext):
        print("ENTER ARG DECL" + ctx.getText())
        self.variables.update({str(ctx.NAME()): (ctx.MUTABLE_TOKEN() is not None)})
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
        print("ENTER STRUCTURAL BLOCK  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#structural_block.
    def exitStructural_block(self, ctx: jjParser.Structural_blockContext):
        print("END STRUCTURAL BLOCK  " + ctx.getText())
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
        print("ENTER STRUCT LINE  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#structural_line.
    def exitStructural_line(self, ctx: jjParser.Structural_lineContext):
        print("END STRUCT LINE  " + ctx.getText())
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

        pass

    # Exit a parse tree produced by jjParser#variable_declaration.
    def exitVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        print("END VAR DEC  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#instruction_line.
    def enterInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        print("ENTER INSTRUCTION LINE  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#instruction_line.
    def exitInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        print("END INSTRUCTION LINE  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#structural_line_instruction.
    def enterStructural_line_instruction(self, ctx: jjParser.Structural_line_instructionContext):
        print("ENTER STRUC LINE INSTRUCTION  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#structural_line_instruction.
    def exitStructural_line_instruction(self, ctx: jjParser.Structural_line_instructionContext):
        print("END STRUC LINE INSTRUCTION  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#statement.
    def enterStatement(self, ctx: jjParser.StatementContext):
        print("ENTER STATEMENT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#statement.
    def exitStatement(self, ctx: jjParser.StatementContext):
        print("END STATEMENT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#instruction.
    def enterInstruction(self, ctx: jjParser.InstructionContext):
        print("ENTER INSTRUCTION  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#instruction.
    def exitInstruction(self, ctx: jjParser.InstructionContext):
        print("END INSTRUCTION  " + ctx.getText())

        pass

    # Enter a parse tree produced by jjParser#expresion_in_parenthesis.
    def enterExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        print("ENTER EXP IN PARENT  " + ctx.getText())
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
        if self.functions_list.get(name) is None:
            raise Exception("NIE ZADEKLROWANO FUNC: " + name)
        pass

    # Exit a parse tree produced by jjParser#function_call.
    def exitFunction_call(self, ctx: jjParser.Function_callContext):
        print("END FUNC CALL  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#identifier.
    def enterIdentifier(self, ctx: jjParser.IdentifierContext):
        print("ENTER ID  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#identifier.
    def exitIdentifier(self, ctx: jjParser.IdentifierContext):
        print("END ID  " + ctx.getText())
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
        print("ENTER IF STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#if_statement.
    def exitIf_statement(self, ctx: jjParser.If_statementContext):
        print("END IF STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#else_statement.
    def enterElse_statement(self, ctx: jjParser.Else_statementContext):
        print("ENTER ELSE STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#else_statement.
    def exitElse_statement(self, ctx: jjParser.Else_statementContext):
        print("END ELSE STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#while_statement.
    def enterWhile_statement(self, ctx: jjParser.While_statementContext):
        print("ENTER WHILE STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#while_statement.
    def exitWhile_statement(self, ctx: jjParser.While_statementContext):
        print("END WHILE STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#for_statement.
    def enterFor_statement(self, ctx: jjParser.For_statementContext):
        print("ENTER FOR STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#for_statement.
    def exitFor_statement(self, ctx: jjParser.For_statementContext):
        print("END FOR STAT  " + ctx.getText())
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
