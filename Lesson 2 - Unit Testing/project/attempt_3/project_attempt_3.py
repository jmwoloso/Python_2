#!/usr/bin/python3
#
# A Truly Modest Program
#    unittest_hw.py
#
# Created by: Jason Wolosonovich
#             02-19-2015
#
# Python 2 - Lesson 2 Project, Attempt 3
"""Demonstrates a possible usage of the unittest module"""
import unittest

#define function to run tests on
def title(s):
    """Manual attempt to mimic str.title()"""
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:].lower()

#defining test suite
class TestTitle(unittest.TestCase):
    
    def test_single_word(self):
        '''Tests title func compared to title method for a single word'''
        s='hELLo'
        msg=("\nTHESE SHOULD MATCH:\n"
             "Built-in Output: {0}\n"
             "Current Output: {1}".format(s.title(), title(s)))
        self.assertEqual(title(s), s.title(), msg)
        
    def test_extra_whitespace(self):
        '''Tests title func compared to built-in method for extra
           whitespace'''
        s=' hELLo'
        msg=("\nTHESE SHOULD NOT MATCH:\n"
             "Built-in Output: {0}\n"
             "Current Output: {1}".format(s.title(), title(s)))
        self.assertNotEqual(title(s), s.title(), msg)
    
    def test_single_contraction(self):
        '''Tests title func compared to built-in method for a
           single word that is a contraction'''
        s='ain\'t'
        msg=("\nTHESE SHOULD NOT MATCH:\n"
             "Built-in Output: {0}\n"
             "Current Output: {1}".format(s.title(), title(s)))
        self.assertNotEqual(title(s), s.title(), msg)
        
    def test_bad_comma_separation(self):
        '''Tests title func compared to built-in method for
           multiple words separated by a comma but incorrectly
           spaced'''
        s='wHY,then'
        msg=("\nTHESE SHOULD NOT MATCH:\n"
             "Built-in Output: {0}\n"
             "Current Output: {1}".format(s.title(), title(s)))
        self.assertNotEqual(title(s), s.title(), msg)
        
    def test_multiple_words(self):
        '''Tests title func compared to built-in method for
           multi-word sentences or phrases'''
        s='do you tHINK tHiS CODE wiLL worK?'
        msg=("\nTHESE SHOULD NOT MATCH:\n"
             "Built-in Output: {0}\n"
             "Current Output: {1}".format(s.title(), title(s)))
        self.assertNotEqual(title(s), s.title(), msg)
        
           
if __name__ == "__main__":
    unittest.main()