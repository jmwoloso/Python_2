#!/usr/bin/python3
#
# Lesson 3 Exercise 3 Message Test Module
#    messagetest.py
#
# Created by: Jason Wolosonovich
#    02-20-2015
#
# Lesson 3, Exercise 3
"""
Demonstrates how Python will try and provide a
message for you if a test fails and you have no
message set to be displayed
"""

import unittest

class DemoCase(unittest.TestCase):
    def testMessage1(self):
        self.assertEqual([1,2,3,4], [1, 2, [3, 4]])
        
if __name__ == "__main__":
    unittest.main()