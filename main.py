import sys
from antlr4 import *
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.out.jjParserListener import jjParserListener
from parser.out.jjVisitor import jjVisitor

def check_initial_errors(program_path, verbose):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()

    listener = jjParserListener(verbose)
    listener.run(tree)

def interprete(program_path, verbose):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()
    
    visitor = jjVisitor(verbose)
    visitor.visit(tree)


if __name__ == "__main__":
    #program_path = "examples/only_main.jj"
    program_path = sys.argv[1]
    check_initial_errors(program_path, verbose = False)
    interprete(program_path, verbose = True)

    #main("examples/functions.jj")
