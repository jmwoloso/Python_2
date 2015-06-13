#!/usr/bin/python3
# A Program to Return A List of Recently Modified Files
#    test_latest.py
#
# Create by: Jason Wolosonovich
#    02-24-2015
#
# Lesson 4 - Exercise 3
"""
Returns a list of recently modified files from a 
particular path.
"""
import unittest
import latest2
import time
import os

# set to True or False depending on whether
# you want to use list comprehensions to
# run the latest2.py program. 
# NOTE: Non-PEP compliant
LIST_COMP=True

# Modify this stem to match your local environment
# for use outside of the virtual environment
PATHSTEM = "v:\\workspace\\FileHandling\\src\\"

class TestLatest(unittest.TestCase):
    
    def setUp(self):
        self.path = PATHSTEM
        self.file_names = ["file.old", 
                           "file.bak", 
                           "file.new"]
        for fn in self.file_names:
            f = open(self.path+fn, 
                     "w")
            f.close()
            time.sleep(1)
            
    def test_latest_no_number(self):
        """
        Ensure that calling the function with no arguments returns
        the single most recently-created file.
        """
        expected = [self.path + "file.new"]
        latest_file = latest2.latest(path=self.path)
        self.assertEqual(latest_file, 
                         expected,)
        
    def test_latest_with_args(self):
        """
        Ensure that calling the function with arguments of 2 and some
        directory returns the two most recently-created files in the directory.
        """
        expected = set([self.path + "file.new",
                        self.path + "file.bak"])
        latest_files = set(latest2.latest(2, 
                                          self.path, 
                                          LIST_COMP))
        self.assertEqual(latest_files, 
                         expected)
        
    def tearDown(self):
        for fn in self.file_names:
            os.remove(self.path + fn)
            
if __name__ == "__main__":
    unittest.main()