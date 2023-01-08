class UnaryOperations:
    def negate(value): return not value

    def minus(value): return -value

    def plus(value): return value


class BinaryOperations:
    def add(left, right): return left + right

    def sub(left, right): return left - right

    def mul(left, right): return left * right

    def div(left, right): return left / right

    def mod(left, right): return left % right

    def eq(left, right): return left == right

    def not_eq(left, right): return left != right

    def less(left, right): return left < right

    def more(left, right): return left > right

    def less_eq(left, right): return left >= right

    def more_eq(left, right): return left <= right

    def or_fn(left, right): return left or right

    def and_fn(left, right): return left and right
