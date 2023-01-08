import os
import sys

from jj import run

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"ERROR usage: python {sys.argv[0]} <program_path> [args]")
        sys.exit(1)

    program_path = sys.argv[1]

    if not os.path.exists(program_path):
        print(f"ERROR: File '{program_path}' does not exist!")
        sys.exit(1)

    run(program_path)
