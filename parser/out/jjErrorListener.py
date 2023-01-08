import sys

from antlr4 import Parser
from antlr4.error.ErrorListener import ErrorListener


def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def print_semantic_error(msg: str, line: int, col: int):
    print("Semantic Error:", msg)
    print("line:", line, ", col:", col)


class jjErrorListener(ErrorListener):
    has_syntax_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_syntax_error = True

        stack = (Parser(recognizer)).getRuleInvocationStack()
        stack.reverse()
        # custom_msg = define_problem(offendingSymbol)

        print_error("Syntax Error!")
        print_error("\tFile: ", recognizer.filename)
        print_error("\tToken ", "\"", offendingSymbol.text, "\"",
                    " line: ", line, ", column: ", column,
                    # "\t\n", custom_msg,
                    "\t\n", msg)
        # print_error("Rule Stack: ", stack)


def define_problem(token):
    text = token.text

    match text:
        case "{":
            return "Variable declaration error"
        case "}":
            return "Variable value error"
        case "mut":
            return "Missing \"let\""
        case "<EOF>":
            return "Reached end of file"
