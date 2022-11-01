import sys
from antlr4 import *
from parser.out.jjLexer import jjLexer
from parser.out.jjParser import jjParser
from parser.out.jjListener import jjListener

if __name__ == "__main__":
    while 1:
        data =  InputStream(input(">>> "))
        lexer = jjLexer(data)
        stream = CommonTokenStream(lexer)
        parser = jjParser(stream)
        tree = parser.expresion()
