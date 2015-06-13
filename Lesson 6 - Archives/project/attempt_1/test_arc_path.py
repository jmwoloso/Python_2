#!/usr/bin/python3
#
# Test Program for arc_path.py
#    test_arc_path.py
#
# Created by: Jason Wolosonovich
#   03-06-2015
#
# Lesson 6 - Project Attempt 1
"""
Testing suite for arc_path.py
"""
import unittest
import os
import tempfile
from shutil import rmtree
from arc_path import arc_path


class TestArcPath(unittest.TestCase):
    """ Tests the functionality of the arc_path function. """
    
    def setUp(self):
        # capture original directory
        self.origdir = os.getcwd()
        # create temporary directory
        self.tempdir = tempfile.mkdtemp("noah's_archive")
        # set temp directory as cwd
        os.chdir(self.tempdir)
        # create subdirectory of temp directory
        self.tempsubdir = os.mkdir("secret_animals")
          
        
    def test_arc_path(self):
        # name of the archive
        self.archive = r"noah's_archive.zip"
        # create these files in the temp directory
        for file in ["turtles.txt",
                     "pythons.py",
                     "sheep.sql",
                     "dogs.docx"]:
            f = open(file, "w").close()
        # populate list for comparison via ugly list comp
        expected = [os.path.join(os.path.basename(os.getcwd()), 
                                 os.path.basename(f)) 
                                 for f in os.listdir(os.getcwd()) 
                                 if os.path.isfile(f)]
        # send path and archive name to function
        observed = arc_path(os.getcwd(), 
                            self.archive)
        self.assertEqual(expected,
                         observed,
                         "\n\nThe lists aren't the same:\
                          \n{0}\n{1}\n".format(expected, 
                                               observed))
        
    def tearDown(self):
        # remove zip file
        os.remove(self.archive)
        # change directories
        os.chdir(self.origdir)
        # remove temp directory
        rmtree(self.tempdir)
                      
        
if __name__ == "__main__":
    unittest.main()
    