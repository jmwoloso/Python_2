#!/usr/bin/python3
#
# A First Test-Driven Development Program (TDD)
#    testadder.py
#
# Created by: Jason Wolosonovich
#    02-20-2015
#
# Python 2 - Lesson 3, Exercise 1
"""
Demonstrates the fundamentals of unittest.
adder() is a function that lets you 'add' integers, strings and lists.
"""

from adder import adder # keep the tested code separate from the tests

import unittest
class TestAdder(unittest.TestCase):
    
    def test_numbers(self):
        msg="3 + 4 should be 7"
        self.assertEqual(adder(3,4), 7, msg)
        
    def test_strings(self):
        msg="x + y should be xy"
        self.assertEqual(adder('x','y'), 'xy', msg)
        
    def test_lists(self):
        msg="[1,2] + [3,4] should be [1,2,3,4]"
        self.assertEqual(adder([1,2],[3,4]), [1,2,3,4], msg)
        
    def test_number_and_string(self):
        msg="1 + two should be 1two"
        self.assertEqual(adder(1,'two'), '1two', msg)
        
    def test_numbers_and_list(self):
        msg="4 + [1,2,3] should be [1,2,3,4]"
        self.assertEqual(adder(4,[1,2,3]), [1,2,3,4], msg)
        
if __name__ == "__main__":
    unittest.main()