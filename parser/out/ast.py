class AST:
    INITIAL_PRECEDENCE = 0

    def __init__(self, left, rest = None): 
        if rest is None:
            stack = [left]
        else: 
            bin_op_fn, prority, right = rest
            stack = [left, (bin_op_fn, prority), right]

        self.stack = []
        for x in stack:
            if isinstance(x, AST):
                self.stack += x.stack
            else:
                self.stack.append(x)

    def get_value(self, args = None):
        if args is None:
            lhs = self.stack.pop(0)
            min_precedence = AST.INITIAL_PRECEDENCE
        else:
            lhs, min_precedence = args

        if len(self.stack) == 0:
            return lhs
        
        while len(self.stack) > 0 and self.stack[0][1] > min_precedence:
            op, prority = self.stack.pop(0)
            rhs = self.stack.pop(0)


            while len(self.stack) > 0 and self.stack[0][1] > prority:
                rhs = self.get_value((rhs, prority))

            self.check_type(lhs, rhs)

            lhs = type(rhs)(op(lhs, rhs))

        return lhs
        
    def check_type(self, lhs, rhs):
        if type(lhs) != type(rhs):
            raise Exception("Type mismatch")