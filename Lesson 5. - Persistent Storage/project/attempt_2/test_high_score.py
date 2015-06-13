#!/usr/bin/python3
#
# Tests the Function Within the high_score.py Module
#    test_high_score.py
#
# Created by: Jason Wolosonovich
#    02-26-2015
#
# Lesson 5 - Project 1, Attempt 2
"""
Tests accuracy of high score function in
high_score.py
"""
import unittest
import os
from high_score import high_score
from tempfile import mkdtemp
from shutil import rmtree
from glob import glob

class TestHighScore(unittest.TestCase):
    
    def setUp(self):
        # get cwd
        self.origdir = os.getcwd()
        # setup test directory
        self.tempdir = mkdtemp()
        # switch to test directory
        os.chdir(self.tempdir)
        
        
    def test_high_score(self):
        """ test high_score function with positive scores. """
        player_score_expected = [("Rick Grimes", 22, 22),  # new entry
                                 ("Rick Grimes", 33.0, 33),  # new high score
                                 ("Daryl Dixon", 22.6, 22), # new entry & high score
                                 ("Daryl Dixon", 4, 22),  # lower score
                                 ("Sophia Peletier", -1, -1), #new entry; negative
                                 ("Sophia Peletier", 0, 0), # new high score
                                 ("Merle Dixon", "16", 16), # new entry; score as string
                                 ("Judith Grimes", "five",  # non-valid entry
                                                   "NaN: Not a valid score")
                                 ] 
        msg = "THESE SHOULD BE EQUAL!"
        for player, score, exp in player_score_expected:
            observed = high_score(player, score)   # function call
            self.assertEqual(exp, 
                             observed, 
                             msg)
     
         
    def tearDown(self):
        os.chdir(self.origdir)
        for f in glob(os.path.join(self.origdir,"walking_dead.*")):
            os.remove(f)
        rmtree(self.tempdir)
             
        
if __name__ == "__main__":
    unittest.main()