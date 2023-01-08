from parser.out.jjErrorListener import print_semantic_error


class AST:
    INITIAL_PRECEDENCE = 0

    def __init__(self, left, rest=None):
        if rest is None:
            stack = [left]
        else:
            bin_op_fn, priority, right = rest
            stack = [left, (bin_op_fn, priority), right]

        self.stack = []
        for x in stack:
            if isinstance(x, AST):
                self.stack += x.stack
            else:
                self.stack.append(x)

    def get_value(self, args=None):
        if args is None:
            lhs = self.stack.pop(0)
            min_precedence = AST.INITIAL_PRECEDENCE
        else:
            lhs, min_precedence = args

        if len(self.stack) == 0:
            return lhs

        while len(self.stack) > 0 and self.stack[0][1] > min_precedence:
            op, priority = self.stack.pop(0)
            rhs = self.stack.pop(0)

            while len(self.stack) > 0 and self.stack[0][1] > priority:
                rhs = self.get_value((rhs, priority))

            self.check_type(lhs, rhs)

            op_result = op(lhs, rhs)
            if isinstance(op_result, bool):
                lhs = op_result
            else:
                lhs = type(rhs)(op_result)

        return lhs

    def check_type(self, lhs, rhs):
        if type(lhs) != type(rhs):
            print_semantic_error(f"Type mismatch in expression. Expected {type(lhs).__name__} but got {type(rhs).__name__}")
            exit(1)
