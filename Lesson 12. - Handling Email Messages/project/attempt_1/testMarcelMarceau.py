#!/usr/bin/python3
#
# Test Suite For Marcel Marceau Program
#    testMarcelMarceau.py
#
# Created by: Jason Wolosonovich
#    03-29-2015
#
# Lesson 11 - Project Attempt 1
"""
Test suite for marcel_marceau.py
"""

import unittest
import os
from shutil import rmtree
from tempfile import mkdtemp, mkstemp
from marcel_marceau import MIMEograph



class testMarcelMarceau(unittest.TestCase):
    """Test suite for testing functionality of marcel_marceau.py"""
    
    def setUp(self):
        """Setup testing environment"""
        # capture cwd
        self.origdir = os.getcwd()
        # create temp directory
        self.tempdir = mkdtemp("outbox")
        # change to tempdir
        os.chdir(self.tempdir)
        # make attachments
        self.attach_1 = mkstemp(suffix=".png")
        self.attach_2 = mkstemp(suffix=".txt")
        # create attachments list with temp files and empty list
        self.attachments = [[self.attach_1, 
                             self.attach_2],
                             []
                            ]
        self.email = 'jmwoloso@asu.edu'
        self.message = 'if you can read this it worked!'
        
        
    def test_MIMEograph_attachments(self):
        """Test MIMEograph function with and without attachments"""
        for items in self.attachments:
            self.test = MIMEograph(self.email, 
                                   self.message, 
                                   items)
            print(self.test)
        
      
    def tearDown(self):
        """Cleanup testing environment"""
        # change back to original directory
        os.chdir(self.origdir)
        # delete temporary directory and files
        rmtree(self.tempdir)
        
    
if __name__=="__main__":
    unittest.main()