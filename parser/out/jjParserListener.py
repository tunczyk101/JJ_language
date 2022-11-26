# Generated from jjParser.g4 by ANTLR 4.11.1
from antlr4 import *


if __name__ is not None and "." in __name__:
    from .logger import Logger
    from .jjParser import jjParser
else:
    from logger import Logger
    from jjParser import jjParser


# This class defines a complete listener for a parse tree produced by jjParser.
class jjParserListener(ParseTreeListener):
    functions_list = {}
    variables = {}

    def __init__(self, verbose = False):
        super().__init__()
        self.logger = Logger(verbose)

    # Enter a parse tree produced by jjParser#prog.
    def enterProg(self, ctx: jjParser.ProgContext):
        self.logger.log("Enter prog")
        pass

    # Exit a parse tree produced by jjParser#prog.
    def exitProg(self, ctx: jjParser.ProgContext):
        self.logger.log("Exit prog")
        self.logger.log(self.functions_list)
        self.logger.log(self.variables)
        pass

    # Enter a parse tree produced by jjParser#global_line.
    def enterGlobal_line(self, ctx: jjParser.Global_lineContext):
        self.logger.log("Global line")
        pass

    # Exit a parse tree produced by jjParser#global_line.
    def exitGlobal_line(self, ctx: jjParser.Global_lineContext):
        self.logger.log("out of global line")
        pass

    # Enter a parse tree produced by jjParser#function.
    def enterFunction(self, ctx: jjParser.FunctionContext):
        self.logger.log("FUNC " + str(ctx.NAME()))
        name = str(ctx.NAME())
        if self.functions_list.get(name) is None:
            self.functions_list.update({name: []})
        else:
            self.logger.log("UPDATE F")

    # Exit a parse tree produced by jjParser#function.
    def exitFunction(self, ctx: jjParser.FunctionContext):
        self.logger.log("END FUNC  " + str(ctx.NAME()))
        self.logger.log()
        self.logger.log(self.variables)
        self.logger.log()
        self.logger.log("$$$$$$$$$$$$$ CLEAR")
        self.vars.clear()
        pass

    # Enter a parse tree produced by jjParser#function_main.
    def enterFunction_main(self, ctx: jjParser.Function_mainContext):
        self.logger.log("MAIN  " + ctx.getText())
        # self.logger.log(self.functions_list.get("main"))
        if self.functions_list.get("main") != None:
            self.logger.log("!!!!!!!!!!!!!!!!!!! TYLKO JEDEN MAIN!!!")
            # exit(1)
        self.functions_list.update({"main": []})
        # self.logger.log(ctx.)
        pass

    # Exit a parse tree produced by jjParser#function_main.
    def exitFunction_main(self, ctx: jjParser.Function_mainContext):
        self.logger.log("OUT MAIN")
        self.variables.clear()
        pass

    # Enter a parse tree produced by jjParser#optinal_function_blocks.
    def enterOptinal_function_blocks(self, ctx: jjParser.Optinal_function_blocksContext):
        self.logger.log("OPTIONAL FUNC BLOCKS  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#optinal_function_blocks.
    def exitOptinal_function_blocks(self, ctx: jjParser.Optinal_function_blocksContext):
        self.logger.log("END OPTIONAL FUNC BLOCKS  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#argument_decl.
    def enterArgument_decl(self, ctx: jjParser.Argument_declContext):
        self.logger.log("ENTER ARG DECL" + ctx.getText())
        self.variables.update({str(ctx.NAME()): (ctx.MUTABLE_TOKEN() is not None)})
        pass

    # Exit a parse tree produced by jjParser#argument_decl.
    def exitArgument_decl(self, ctx: jjParser.Argument_declContext):
        self.logger.log("END ARG DECL " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#additional_arguments_decl.
    def enterAdditional_arguments_decl(self, ctx: jjParser.Additional_arguments_declContext):
        self.logger.log("ENTER ADD ARG " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#additional_arguments_decl.
    def exitAdditional_arguments_decl(self, ctx: jjParser.Additional_arguments_declContext):
        self.logger.log("END ADD ARG " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#arguments_block.
    def enterArguments_block(self, ctx: jjParser.Arguments_blockContext):
        self.logger.log("ARG BLOCK  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#arguments_block.
    def exitArguments_block(self, ctx: jjParser.Arguments_blockContext):
        self.logger.log("END ARG BLOCK")
        pass

    # Enter a parse tree produced by jjParser#structural_block.
    def enterStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.logger.log("ENTER STRUCTURAL BLOCK  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#structural_block.
    def exitStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.logger.log("END STRUCTURAL BLOCK  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#return_block.
    def enterReturn_block(self, ctx: jjParser.Return_blockContext):
        self.logger.log("ENTER RETURN  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#return_block.
    def exitReturn_block(self, ctx: jjParser.Return_blockContext):
        self.logger.log("END RETURN  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#guard_block.
    def enterGuard_block(self, ctx: jjParser.Guard_blockContext):
        self.logger.log("ENTER GUARD  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#guard_block.
    def exitGuard_block(self, ctx: jjParser.Guard_blockContext):
        self.logger.log("END GUARD  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#structural_line.
    def enterStructural_line(self, ctx: jjParser.Structural_lineContext):
        self.logger.log("ENTER STRUCT LINE  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#structural_line.
    def exitStructural_line(self, ctx: jjParser.Structural_lineContext):
        self.logger.log("END STRUCT LINE  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#variable_declaration.
    def enterVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        self.logger.log("ENTER VAR DEC  " + ctx.getText())
        # self.logger.log(ctx.MUTABLE_TOKEN())
        name = str(ctx.NAME())
        if self.variables.get(name) != None:
            self.logger.log("!!!!! PONOWNA DEKLARACJA ZMIENNEJ: " + name)
            # exit(1)
        self.variables.update({name: (ctx.MUTABLE_TOKEN() is not None)})

        pass

    # Exit a parse tree produced by jjParser#variable_declaration.
    def exitVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        self.logger.log("END VAR DEC  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#instruction_line.
    def enterInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        self.logger.log("ENTER INSTRUCTION LINE  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#instruction_line.
    def exitInstruction_line(self, ctx: jjParser.Instruction_lineContext):
        self.logger.log("END INSTRUCTION LINE  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#structural_line_instruction.
    def enterStructural_line_instruction(self, ctx: jjParser.Structural_line_instructionContext):
        self.logger.log("ENTER STRUC LINE INSTRUCTION  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#structural_line_instruction.
    def exitStructural_line_instruction(self, ctx: jjParser.Structural_line_instructionContext):
        self.logger.log("END STRUC LINE INSTRUCTION  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#statement.
    def enterStatement(self, ctx: jjParser.StatementContext):
        self.logger.log("ENTER STATEMENT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#statement.
    def exitStatement(self, ctx: jjParser.StatementContext):
        self.logger.log("END STATEMENT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#instruction.
    def enterInstruction(self, ctx: jjParser.InstructionContext):
        self.logger.log("ENTER INSTRUCTION  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#instruction.
    def exitInstruction(self, ctx: jjParser.InstructionContext):
        self.logger.log("END INSTRUCTION  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#expresion_in_parenthesis.
    def enterExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        self.logger.log("ENTER EXP IN PARENT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#expresion_in_parenthesis.
    def exitExpresion_in_parenthesis(self, ctx: jjParser.Expresion_in_parenthesisContext):
        self.logger.log("END EXP IN PARENT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#left_of_binary_operation.
    def enterLeft_of_binary_operation(self, ctx: jjParser.Left_of_binary_operationContext):
        self.logger.log("ENTER BIN OP  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#left_of_binary_operation.
    def exitLeft_of_binary_operation(self, ctx: jjParser.Left_of_binary_operationContext):
        self.logger.log("END BIN OP  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#all_binary_operations.
    def enterAll_binary_operations(self, ctx: jjParser.All_binary_operationsContext):
        self.logger.log("ENTER ALL BIN OP  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#all_binary_operations.
    def exitAll_binary_operations(self, ctx: jjParser.All_binary_operationsContext):
        self.logger.log("END ALL BIN OP  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#all_unary_operations.
    def enterAll_unary_operations(self, ctx: jjParser.All_unary_operationsContext):
        self.logger.log("ENTER ALL UNARY OP  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#all_unary_operations.
    def exitAll_unary_operations(self, ctx: jjParser.All_unary_operationsContext):
        self.logger.log("END ALL UNARY OP  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#expresion.
    def enterExpresion(self, ctx: jjParser.ExpresionContext):
        self.logger.log("ENTER EX  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#expresion.
    def exitExpresion(self, ctx: jjParser.ExpresionContext):
        self.logger.log("END EX  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#function_call.
    def enterFunction_call(self, ctx: jjParser.Function_callContext):
        self.logger.log("ENTER FUNC CALL  " + ctx.getText())
        name = str(ctx.NAME())
        if self.functions_list.get(name) is None:
            #raise Exception("NIE ZADEKLROWANO FUNC: " + name)
            pass

    # Exit a parse tree produced by jjParser#function_call.
    def exitFunction_call(self, ctx: jjParser.Function_callContext):
        self.logger.log("END FUNC CALL  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#identifier.
    def enterIdentifier(self, ctx: jjParser.IdentifierContext):
        self.logger.log("ENTER ID  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#identifier.
    def exitIdentifier(self, ctx: jjParser.IdentifierContext):
        self.logger.log("END ID  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#value.
    def enterValue(self, ctx: jjParser.ValueContext):
        self.logger.log("ENTER VAL  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#value.
    def exitValue(self, ctx: jjParser.ValueContext):
        self.logger.log("END VAL  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#if_statement_start.
    def enterIf_statement_start(self, ctx: jjParser.If_statement_startContext):
        self.logger.log("ENTER STAT START  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#if_statement_start.
    def exitIf_statement_start(self, ctx: jjParser.If_statement_startContext):
        self.logger.log("END STAT START  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#if_statement.
    def enterIf_statement(self, ctx: jjParser.If_statementContext):
        self.logger.log("ENTER IF STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#if_statement.
    def exitIf_statement(self, ctx: jjParser.If_statementContext):
        self.logger.log("END IF STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#else_statement.
    def enterElse_statement(self, ctx: jjParser.Else_statementContext):
        self.logger.log("ENTER ELSE STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#else_statement.
    def exitElse_statement(self, ctx: jjParser.Else_statementContext):
        self.logger.log("END ELSE STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#while_statement.
    def enterWhile_statement(self, ctx: jjParser.While_statementContext):
        self.logger.log("ENTER WHILE STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#while_statement.
    def exitWhile_statement(self, ctx: jjParser.While_statementContext):
        self.logger.log("END WHILE STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#for_statement.
    def enterFor_statement(self, ctx: jjParser.For_statementContext):
        self.logger.log("ENTER FOR STAT  " + ctx.getText())
        pass

    # Exit a parse tree produced by jjParser#for_statement.
    def exitFor_statement(self, ctx: jjParser.For_statementContext):
        self.logger.log("END FOR STAT  " + ctx.getText())
        pass

    # Enter a parse tree produced by jjParser#assignmnet_statement.
    def enterAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        self.logger.log("ENTER ASSIG STAT  " + ctx.getText())

        name = str(ctx.NAME())

        if self.variables.get(name) is None:
            raise Exception("NIE ZADEKLAROWANO ZMIENNEJ: " + name)

        elif not self.variables.get(name):
            # self.logger.log("!!!!!!!!!!!!!!! ZMIENNA NIE JEST ZMIENNA")
            raise Exception("ZMIENNA: " + name + " NIE JEST ZMIENNA")

    # Exit a parse tree produced by jjParser#assignmnet_statement.
    def exitAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        self.logger.log("END ASSIG STAT  " + ctx.getText())
        pass

    def run(self, node):
        self.logger.log("run")
        self.vars = {}
        self.stack = []
        self.functions = {}
        ParseTreeWalker().walk(self, node)


del jjParser
