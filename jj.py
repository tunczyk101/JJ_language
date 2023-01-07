from antlr4 import *

from parser.out.jjErrorListener import jjErrorListener
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.out.jjListener import jjListener
from parser.out.jjVisitor import jjVisitor


def check_initial_errors(program_path: str, verbose: bool):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)

    parser.removeErrorListeners()
    error_listener = jjErrorListener()
    parser.addErrorListener(error_listener)

    tree = parser.prog()

    if error_listener.has_syntax_error:
        return True

    listener = jjListener(verbose)
    listener.run(tree)

    return False


def interpret(program_path: str):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()

    visitor = jjVisitor()
    visitor.visit(tree)


def run(program_path: str):
    if not check_initial_errors(program_path, verbose=False):
        interpret(program_path)

