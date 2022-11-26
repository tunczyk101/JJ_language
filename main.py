import sys
from antlr4 import *
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.out.jjParserListener import jjParserListener

def main(argv):
    print(argv[1])
    data = FileStream(argv[1])
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()
    listener = jjParserListener(verbose=True)
    listener.run(tree)


if __name__ == "__main__":
    # main(sys.argv)
    x = "examples/functions.jj"
    main([0, x])
