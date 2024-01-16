import json
import unittest
from handin import *

## Change here
UNIT_UNDER_TEST="Grains on a Chessboard"

class TestCases(unittest.TestCase):

    fname = UNIT_UNDER_TEST
    success_count = 0
    total_tests = 0

    def test_zero_raises_error(self):
        with self.assertRaises(ValueError) as err:
            square(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Square number out of range")

    def test_65_raises_error(self):
        with self.assertRaises(ValueError) as err:
            square(65)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Square number out of range")

    def all_tests(self):

        print(f"Testing {self.fname} ...")

##        try:
##            print(f"*** Checking CONSTANT...")
##            self.total_tests = self.total_tests + 1
##            in1=0
##            out=40
##            result=EXPECTED_COOK_TIME
##            assert result == out, "Expected Output: 40"
##            self.success_count = self.success_count + 1
##            print(f"{self.success_count} Pass.")
##            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
##        except AssertionError:
##            print("### Error! Ouput does not match expected value.")
##            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
            
        try:
            print(f"*** Checking square()...")
            self.total_tests = self.total_tests + 1
            in1=1
            out=1
            result=square(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            self.total_tests = self.total_tests + 1
            in1=4
            out=8
            result=square(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            self.total_tests = self.total_tests + 1
            in1=13
            out=4096
            result=square(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
            
        try:
            self.total_tests = self.total_tests + 1
            in1=60
            out=576460752303423488
            result=square(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            self.total_tests = self.total_tests + 1
            self.test_zero_raises_error()
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {0}. Expected Output: ValueError. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            self.total_tests = self.total_tests + 1
            self.test_65_raises_error()
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {65}. Expected Output: ValueError. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

### Test object
test_object = TestCases()
test_object.all_tests()
if test_object.success_count == test_object.total_tests:
    print(f"*** Nice! All the {test_object.success_count} Tests Cleared !!! *** ")
    print(json.dumps({'scores':{'Pass':10}}))
else :
    print(f"### {test_object.success_count} out of {test_object.total_tests} tests successfull ### ")
    print("### Correct the errors and resubmit ###")
