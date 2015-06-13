#!/usr/bin/python3
# A Program to Test Built-in File Handling
#    test_fileops.py
#
# Created by: Jason Wolosonovich
#    02-23-2015
#
# Lesson 4 - Exercise 1
"""
Demonstrates some of the file handling capabilities built-in to python
"""
import unittest
import os
import fileops

class TestReadWriteFile(unittest.TestCase):
    """Test case to verify list read/write functionality."""
    
    def setUp(self):
        """This function is run before each test."""
        self.fixture_file = r"v:\workspace\FileHandling\src\test-read-write.txt"
        self.fixture_list = ["my", 
                             "written", 
                             "text"]
        self.fixture_list_empty_strings = ["my", 
                                           "", 
                                           "", 
                                           "written", 
                                           "text"]
        self.fixture_list_trailing_empty_strings = ["my", 
                                                    "written", 
                                                    "text", 
                                                    "", 
                                                    ""]
        
    def verify_file(self, fixture_list):
        """Verifies that a given list, when written to a file,
        is returned by reading the same file."""
        fileops.write_list(self.fixture_file, 
                           fixture_list)
        observed = fileops.read_list(self.fixture_file)
        self.assertEqual(observed, 
                         fixture_list, 
                         "{0} does not equal {1}".format(observed, 
                                                         fixture_list))
              
    def test_read_write_list(self):
        self.verify_file(self.fixture_list)
        
    def test_read_write_list_empty_strings(self):
        self.verify_file(self.fixture_list_empty_strings)
        
    def test_read_write_list_trailing_empty_strings(self):
        self.verify_file(self.fixture_list_trailing_empty_strings)
        
    def tearDown(self):
        """This function is run after each test."""
        try:
            os.remove(self.fixture_file)
        except OSError:
            pass
        
if __name__ == "__main__":
    unittest.main()