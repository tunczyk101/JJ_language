import sys
# import antlr4
from antlr4 import *
from parser.out.jj import jj
from parser.out.jj_lexer import jj_lexer
from parser.out.jjListener import jjListener

if __name__ == "__main__":
    print("sss")
    while 1:
        data = InputStream(input(">>> "))
        lexer = jj_lexer(data)
        stream = CommonTokenStream(lexer)
        parser = jj(stream)
        tree = parser.expresion()
        listener = jjListener()
    #     listener.run(tree)~~