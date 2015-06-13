#!/usr/bin/python3
#
# Tests the Function Within the high_score.py Module
#    test_high_score.py
#
# Created by: Jason Wolosonovich
#    02-26-2015
#
# Lesson 5 - Project 1, Attempt 1
"""
Tests accuracy of high score function in
high_score.py
"""
import unittest
import os
import shelve
from glob import iglob
from high_score import high_score



class TestHighScore(unittest.TestCase):
    
    def setUp(self):
        # test shelf setup
        self.temp_shelf = shelve.open(r"v:\workspace\PersistentStorage_Homework\src\walking_dead.shlf",
                                      writeback=True)
        
                
    def test_high_score(self):
        # test high_score function
        # Walking Dead Seasons 1,2 & 3 zombie kills for Rick Grimes
        for player_record in [("Rick Grimes", 33),
                              ("Rick Grimes", 22),
                              ("Rick Grimes", 32),
                              ]:
            observed = high_score(self.temp_shelf, *player_record)
        actual = ("Rick Grimes", 33)   # tuple; (player, high_score)
        self.assertEqual(actual, 
                         observed, 
                         "These should be equal!")   
        
    def tearDown(self):
        self.temp_shelf.close()
        for file in iglob("walking_dead.*"):
            os.remove(file)
        
        
if __name__ == "__main__":
    unittest.main()