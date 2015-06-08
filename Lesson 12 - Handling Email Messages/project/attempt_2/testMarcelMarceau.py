#!/usr/bin/python3
#
# Test Suite For Marcel Marceau Program
#    testMarcelMarceau.py
#
# Created by: Jason Wolosonovich
#    03-29-2015
#
# Lesson 11 - Project Attempt 2
"""
Test suite for marcel_marceau.py
"""

import unittest
import os
from marcel_marceau import MIMEograph



class testMarcelMarceau(unittest.TestCase):
    """Test suite for testing functionality of marcel_marceau.py"""
    
    def setUp(self):
        """Setup testing environment"""
        self.attach_1 = [os.path.abspath("picture.png")]
        self.attach_2 = []
        self.attach_3 = [os.path.abspath("zip.gz")]
        self.attachments = [self.attach_1,
                            self.attach_2,
                            self.attach_3]
        self.email = 'jmwoloso@asu.edu'
        self.message = 'if you can read this it *looks like* it worked \n :D'
                               
        
    def test_MIMEograph_attachments(self):
        """Test MIMEograph function with and without attachments"""
        for items in self.attachments:
            self.test = MIMEograph(self.email, 
                                   self.message, 
                                   items)
            print(self.test)
            print("#"*16 + "END TEST" + "#"*16)
        
      
    def tearDown(self):
        """Nothing to cleanup"""
        pass
                
    
if __name__=="__main__":
    unittest.main()