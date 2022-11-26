class Logger:
    def __init__(self, verbose):
        self.verbose = verbose

    def log(self, *args):
        if self.verbose:
            print(','.join(['{}'] * len(args)).format(*args))
