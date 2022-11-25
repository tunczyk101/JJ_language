import sys
from antlr4 import *
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.old_out.jj_lexer import jj_lexer
from parser.out.jjParserListener import jjParserListener

def main(argv):
    print(argv[1])
    data = FileStream(argv[1])
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.prog()
    listener = jjParserListener()
    listener.run(tree)
    # pass


if __name__ == "__main__":
    # print(chr(ord('a')))
    # main(sys.argv)
    x = "examples/only_main.jj"
    main([0, x])
