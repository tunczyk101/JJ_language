import unittest
import subprocess
import os

from jj import run

TEST_PROGRAMS_PATH = "examples"
TEST_RESULTS_PATH = "examples_results"
RESULT_SUFIX = ".out"
JJ_SUFIX = ".jj"


class JJTests(unittest.TestCase):
    def __init__(self, program_names):
        super().__init__()
        self.program_names = program_names

    def runTest(self):
        for program_name in self.program_names:
            with self.subTest(f"Testing '{program_name}'"):
                print(f"Testing '{program_name}'")
                out = subprocess.check_output(['python3.10', 'main.py',  TEST_PROGRAMS_PATH + os.path.sep + program_name])
                
                with open(TEST_RESULTS_PATH + os.path.sep + program_name + RESULT_SUFIX, "r") as f:
                     expected_output = f.read()
                
                self.assertEqual(expected_output, out.decode("utf-8"))
        

def get_all_files_ended_with(root_path: str, sufix: str):
    results = []

    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith(sufix):
                results.append((root + os.path.sep + file)[len(root_path) + len(os.path.sep):])

    return results





def suite():
    suite = unittest.TestSuite()


    programs_results = get_all_files_ended_with(TEST_RESULTS_PATH, RESULT_SUFIX)
    all_programs = get_all_files_ended_with(TEST_PROGRAMS_PATH, JJ_SUFIX)

    programs_to_test = []
    for program_name in all_programs:
        if program_name + RESULT_SUFIX in programs_results:
            programs_to_test.append(program_name)

    suite.addTest(JJTests(programs_to_test))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())