#!/usr/bin/python3
#
# Lesson 3 Exercise 2 setUp Demo Module
#    setUpDemo.py
#
# Created by: Jason Wolosonovich
#    02-20-2015
#
# Lesson 3, Exercise 2
"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        msg="Created"
        #save the current directory to the origdir instance
        self.origdir = os.getcwd()
        #creates a new empty directory
        self.dirname = tempfile.mkdtemp("testdir")
        #confirm creation and show path to created directory
        #this code is commented out because when run, it muddies up
        #the testing output -- removed for clarity
        #print(msg, self.dirname)
        #set current directory to created directory
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible"
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
            
    def test_2(self):
        "Verify that the current directory is empty"
        msg="Directory not empty"
        self.assertEqual(glob.glob("*"), [], msg)
        
    def tearDown(self):
        msg="Deleted"
        #changes current directory back to original directory
        os.chdir(self.origdir)
        #removes created directory and any contents inside
        shutil.rmtree(self.dirname)
        #this code is commented out because when run, it muddies up
        #the testing output -- removed for clarity
        #print(msg, self.dirname)
            
if __name__ == "__main__":
    unittest.main()