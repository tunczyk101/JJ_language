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
        print(stack)
        print(offendingSymbol)
        print(msg)
        print(e)
        custom_msg = define_problem(msg, offendingSymbol.text)

        print_error("Syntax Error!")
        print_error("\tFile: ", recognizer.filename)
        print_error("\tToken ", "\"", offendingSymbol.text, "\"",
                    " line: ", line, ", column: ", column,
                    "\t\n", custom_msg,
                    "\t\n", msg
                    )
        exit(1);
        # print_error("Rule Stack: ", stack)


def define_problem(text, token):
    match text:
        case "mismatched input '{' expecting {'mut', NAME}" | "missing NAME at '{'":
            return "Variable name needed"
        case "mismatched input '}' expecting {NUMBER_TYPE, BOOL, '(', UNARY_OR_BINARY_OPERATIONS, '!', '^', NAME}":
            return "Variable needs value"

    if "mismatched input" in text or "extraneous input" in text:
        miss = ""
        l = len(text) - 2
        while text[l] != "'" or l < 7:
            miss = text[l] + miss
            l -= 1
        return "missing " + miss

    temp = text[:len(text) - len(" '' at" + token)]

    if "missing" in temp:
        return temp

    return ""
