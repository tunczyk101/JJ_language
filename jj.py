from antlr4 import *
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.out.jjListener import jjListener
from parser.out.jjVisitor import jjVisitor

def check_initial_errors(program_path: str, verbose: bool):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    listener = jjListener(verbose)

    tree = parser.prog()
    listener.run(tree)


def interpret(program_path: str):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()
    
    visitor = jjVisitor()
    visitor.visit(tree)

def run(program_path: str):
    check_initial_errors(program_path, verbose=False)
    interpret(program_path)
