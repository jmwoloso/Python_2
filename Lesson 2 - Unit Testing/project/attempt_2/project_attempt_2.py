#!/usr/bin/python3
#
# A Truly Modest Program
#    unittest_hw.py
#
# Created by: Jason Wolosonovich
#             02-19-2015
#
# Python 2 - Lesson 2 Project, Attempt 2
"""Demonstrates a possible usage of the unittest module"""
import unittest

#code to be tested
s = "hELLo"

def title(s):
    """Manual attempt to mimic str.title()"""
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:].lower()

#defining test suite
class TestTitle(unittest.TestCase):
    
    def test_title_func(self):
        '''Tests effectiveness of title function relative to s.title()'''
        msg=("\nThese should match:\n"
             "Correct Output: {0}\n"
             "Current Output: {1}".format(s.title(), title(s)))
        self.assertEqual(title(s), s.title(), msg)

if __name__ == "__main__":
    unittest.main()