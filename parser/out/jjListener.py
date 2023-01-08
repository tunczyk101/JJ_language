from dataclasses import dataclass
from typing import Any

from antlr4 import *

if __name__ is not None and "." in __name__:
    from .logger import Logger
    from .jjParser import jjParser
    from .jjErrorListener import print_semantic_error
    from .jjParserListener import jjParserListener
    from .functions import STANDARD_FUNCTIONS
else:
    from logger import Logger
    from jjParser import jjParser
    from jjErrorListener import print_semantic_error
    from jjParserListener import jjParserListener
    from functions import STANDARD_FUNCTIONS


@dataclass
class Variable:
    is_mutable: bool
    name: str
    scope: Any


# This class defines a complete listener for a parse tree produced by jjParser.
class jjListener(jjParserListener):
    functions_list = {}
    variables = []
    statements = {}
    curr_function = None

    def __init__(self, verbose=False):
        super().__init__()
        self.logger = Logger(verbose)

    # Exit a parse tree produced by jjParser#prog.
    def exitProg(self, ctx: jjParser.ProgContext):
        self.logger.log(self.functions_list)
        self.logger.log(self.variables)
        if self.functions_list.get("main") is None:
            print_semantic_error("Main is not defined")
            exit(0)

    # Enter a parse tree produced by jjParser#function.
    def enterFunction(self, ctx: jjParser.FunctionContext):
        self.logger.log("FUNC " + str(ctx.NAME()))
        name = str(ctx.NAME())
        # self.logger.log(ctx. )
        self.statements.update({ctx: []})

        if self.functions_list.get(name) is None:
            self.functions_list.update({name: []})
            self.curr_function = ctx

    # Exit a parse tree produced by jjParser#function.
    def exitFunction(self, ctx: jjParser.FunctionContext):
        self.logger.log("EXIT FUNC " + ctx.getText())
        for i in range(len(self.variables) - 1, -1, -1):
            if self.variables[i].scope == ctx:
                self.variables.pop(i)

    # Enter a parse tree produced by jjParser#function_main.
    def enterFunction_main(self, ctx: jjParser.Function_mainContext):
        self.logger.log("Main")
        if self.functions_list.get("main") is not None:
            print_semantic_error("Multiple declarations of main function")
            exit(1)
        self.functions_list.update({"main": []})
        self.statements.update({ctx: []})
        self.curr_function = ctx

    # Exit a parse tree produced by jjParser#function_main.
    def exitFunction_main(self, ctx: jjParser.Function_mainContext):
        self.variables.clear()

    # Enter a parse tree produced by jjParser#argument_decl.
    def enterArgument_decl(self, ctx: jjParser.Argument_declContext):
        self.logger.log("ENTER ARG DECL" + ctx.getText())
        curr_scope = list(self.statements.keys())[-1]
        name = str(ctx.NAME())

        self.checkVariableExistence(name, curr_scope)

        self.variables.append(Variable(
            is_mutable=ctx.MUTABLE_TOKEN() is not None,
            name=name,
            scope=curr_scope
        ))

    def checkVariableExistence(self, name, curr_scope):
        for var in reversed(self.variables):
            if var.name == name and var.scope == curr_scope:
                print_semantic_error("Variable " + name + " already exists")
                exit(0)

    # Enter a parse tree produced by jjParser#variable_declaration.
    def enterVariable_declaration(self, ctx: jjParser.Variable_declarationContext):
        self.logger.log("ENTER VAR DEC  " + ctx.getText())
        name = str(ctx.NAME())
        curr_scope = list(self.statements.keys())[-1]

        self.checkVariableExistence(name, curr_scope)

        self.variables.append(Variable(
            is_mutable=ctx.MUTABLE_TOKEN() is not None,
            name=name,
            scope=list(self.statements.keys())[-1]
        ))
        self.logger.log("dodano  " + ctx.getText())

    # Enter a parse tree produced by jjParser#function_call.
    def enterFunction_call(self, ctx: jjParser.Function_callContext):
        self.logger.log("ENTER FUNC CALL  " + ctx.getText())
        name = str(ctx.NAME())
        if self.functions_list.get(name) is None and name not in STANDARD_FUNCTIONS:
            print_semantic_error("Semantic error: Func " + name + " not defined")
            exit(0)

    # Enter a parse tree produced by jjParser#if_statement.
    def enterIf_statement(self, ctx: jjParser.If_statementContext):
        self.statements.update({ctx: []})

    def enterStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.statements.update({ctx: []})

    def exitStructural_block(self, ctx: jjParser.Structural_blockContext):
        self.clear_scope_var(ctx)

    # Exit a parse tree produced by jjParser#if_statement.
    def exitIf_statement(self, ctx: jjParser.If_statementContext):
        self.clear_scope_var(ctx)

    # Enter a parse tree produced by jjParser#else_statement.
    def enterElse_statement(self, ctx: jjParser.Else_statementContext):
        self.statements.update({ctx: []})

    # Exit a parse tree produced by jjParser#else_statement.
    def exitElse_statement(self, ctx: jjParser.Else_statementContext):
        self.clear_scope_var(ctx)

    # Enter a parse tree produced by jjParser#while_statement.
    def enterWhile_statement(self, ctx: jjParser.While_statementContext):
        self.statements.update({ctx: []})

    # Exit a parse tree produced by jjParser#while_statement.
    def exitWhile_statement(self, ctx: jjParser.While_statementContext):
        self.clear_scope_var(ctx)

    # Enter a parse tree produced by jjParser#for_statement.
    def enterFor_statement(self, ctx: jjParser.For_statementContext):
        self.statements.update({ctx: []})

    # Exit a parse tree produced by jjParser#for_statement.
    def exitFor_statement(self, ctx: jjParser.For_statementContext):
        self.clear_scope_var(ctx)

    # Enter a parse tree produced by jjParser#assignmnet_statement.
    def enterAssignmnet_statement(self, ctx: jjParser.Assignmnet_statementContext):
        name = str(ctx.NAME())

        for var in reversed(self.variables):
            if var.name == name:
                if not var.is_mutable:
                    print_semantic_error("Variable " + name + " is not mut")
                    exit(0)
                return

        print_semantic_error(name + " is not defined")
        exit(0)

    def enterIdentifier(self, ctx: jjParser.IdentifierContext):
        name = ctx.NAME()
        if name is not None:
            name = str(name)
            for var in self.variables:
                if var.name == name:
                    return
            print_semantic_error(name + " is not defined")
            exit(0)

    def clear_scope_var(self, ctx):
        for i in range(len(self.variables) - 1, -1, -1):
            if self.variables[i].scope == ctx:
                self.variables.pop(i)

        self.statements.pop(ctx)

    def run(self, node):
        self.logger.log("run")
        ParseTreeWalker().walk(self, node)


del jjParser
