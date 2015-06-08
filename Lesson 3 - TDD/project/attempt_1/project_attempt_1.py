#!/usr/bin/python3
#
# Lesson 3 Exercise 2 setUp Demo Module
#    setupDemo.py
#
# Created by: Jason Wolosonovich
#    02-20-2015
#
# Lesson 3 - Project, Attempt 1
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
        set_em_up = set(["this.txt", "that.txt", "the_other.txt"])
        knock_em_down = set() #empty set for updating after file creation
        msg=("\nYOUR SETS DO NOT MATCH:\n"
             "Specified File Names: {0}\n"
             "Actual File Names: {1}".format(set_em_up, knock_em_down))
        for filename in set_em_up:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        knock_em_down.update(os.listdir()) #update the set with file names
        self.assertSetEqual(set_em_up,
                            knock_em_down,
                            msg) #compare sets
            
    def test_2(self):
        "Verify that the current directory is empty"
        msg="Directory not empty"
        self.assertEqual(glob.glob("*"), [], msg)
        
    def test_3(self):
        "Create binary file 1 millllllllion bytes long"
        filename = "this_bytes"
        byte_me = " " * 1000000 #write bytes as whitespace
        file_size = 1000000 #file size target
        f = open(filename,"w")
        f.write(byte_me)
        f.close()
        self.assertTrue(f.closed)
        e = os.stat(filename) #get stat info
        self.assertEqual(e.st_size,
                         file_size,
                         ("\nYOUR FILE SIZES DO NOT MATCH:\n"
                          "Actual File Size: {0}\n"
                          "Target File Size: {1}".format(e.st_size,
                                                         file_size)))
        
    def tearDown(self):
        #msg="Deleted"
        #changes current directory back to original directory
        os.chdir(self.origdir)
        #removes created directory and any contents inside
        shutil.rmtree(self.dirname)
        #this code is commented out because when run, it muddies up
        #the testing output -- removed for clarity
        #print(msg, self.dirname)
            
if __name__ == "__main__":
    unittest.main()