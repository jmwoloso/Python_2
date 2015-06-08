#!/usr/bin/python3
#
# A Program That Tests the ClassFactory Function
#    testClassFactory.py
#
# Created by: Jason Wolosonovich
#    03-20-2015
#
# Lesson 11 - Exercise 4
"""
Testing module for the ClassFactory function.
"""

import unittest
from classFactory import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):
        # create DataRow object
        C = build_row("user", "id name email")
        # create instance of DataRow class
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
        
    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")

if __name__=="__main__":
    unittest.main()