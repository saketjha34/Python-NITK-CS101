import json
import unittest
from handin import *

## Change here
UNIT_UNDER_TEST="Mysore Pak Cookbook"

class TestCases(unittest.TestCase):

    fname = UNIT_UNDER_TEST
    success_count = 0
    total_tests = 0

    def test_zero_pieces_raises_error(self):
        with self.assertRaises(ValueError) as err:
            preparation_time_required_in_minutes(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Number of pieces should be greater than Zero.")

    def all_tests(self):

        print(f"Testing {self.fname} ...")

        try:
            print(f"*** Checking CONSTANT...")
            self.total_tests = self.total_tests + 1
            in1=0
            out=40
            result=EXPECTED_COOK_TIME
            assert result == out, "Expected Output: 40"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
            
        try:
            print(f"*** Checking cooking_time_remaining()...")
            self.total_tests = self.total_tests + 1
            in1=25
            out=15
            result=cooking_time_remaining(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
            
        try:
            self.total_tests = self.total_tests + 1
            in1=0
            out=40
            result=cooking_time_remaining(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            print(f"*** Checking preparation_time_required_in_minutes()...")
            self.total_tests = self.total_tests + 1
            in1=40
            out=20
            result=preparation_time_required_in_minutes(in1)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

##        try:
##            self.total_tests = self.total_tests + 1
##            self.test_zero_pieces_raises_error()
##            self.success_count = self.success_count + 1
##            print(f"{self.success_count} Pass.")
##            print(f"Input: {0}. Expected Output: ValueError. \n")
##
####            in1=0
####            out=0
####            
######            result=preparation_time_required_in_minutes(in1)
####            assert result == out, f"Expected Output: {out}"
####
##            
##        except AssertionError:
##            print("### Error! Ouput does not match expected value.")
##            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            print(f"*** Checking remaining_time_in_minutes()...")
            self.total_tests = self.total_tests + 1
            in1=20
            in2=17
            out=33
            result=remaining_time_in_minutes(in1, in2)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
        except AssertionError:
            print("### Error! Ouput does not match expected value.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")

        try:
            self.total_tests = self.total_tests + 1
            in1=20
            in2=100
            out=0
            result=remaining_time_in_minutes(in1, in2)
            assert result == out, f"Expected Output: {out}"
            self.success_count = self.success_count + 1
            print(f"{self.success_count} Pass.")
            print(f"Input: {in1}. Expected Output:{out}. Function Output: {result}. \n")
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
