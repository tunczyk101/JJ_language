import sys

from antlr4 import Parser, Token
from antlr4.error.ErrorListener import ErrorListener


def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class jjErrorListener(ErrorListener):
    has_syntax_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_syntax_error = True

        stack = (Parser(recognizer)).getRuleInvocationStack()
        stack.reverse()
        print_error("Syntax Error!")
        print_error("Token ", "\"", offendingSymbol.text, "\"",
                    "line: ", line, ", column: ", column,
                    "\n", msg)
        # print_error("Rule Stack: ", stack)
