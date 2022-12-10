import sys
from antlr4 import *
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.out.jjListener import jjListener
from parser.out.jjVisitor import jjVisitor

def check_initial_errors(program_path, verbose):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()

    listener = jjListener(verbose)
    listener.run(tree)

def interprete(program_path):
    data = FileStream(program_path)
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()
    
    visitor = jjVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    program_path = "examples/statements/for_loop.jj"
    # program_path = sys.argv[1]
    check_initial_errors(program_path, verbose=False)
    print("interprete")
    interprete(program_path)

    #main("examples/functions.jj")
