import sys
from antlr4 import *
from parser.out.jjParser import jjParser
from parser.out.jjLexer import jjLexer
from parser.out.jjParserListener import jjParserListener

def main(argv):
    data = FileStream(argv[1])
    lexer = jjLexer(data)
    stream = CommonTokenStream(lexer)
    parser = jjParser(stream)
    tree = parser.expresion()
    listener = jjParserListener()
    listener.run(tree)
    # pass

if __name__ == "__main__":
    print(chr(ord('a')))
    main(sys.argv)
    # y = [chr(i) for i in x]
    # print(y)
    # for i in range(1):
    #     # print(i)
    #     if x[i] != ord(y[i]):
    #         print(i, "!=", ord(y[i]))
    #     else:
    #         print(chr(x[i]))
