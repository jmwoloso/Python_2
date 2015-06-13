#!/usr/bin/python3
#
# A Program to Keep Track of High Scores by Player
#    high_score.py
#
# Created by: Jason Wolosonovich
#    02-26-2015
#
# Lesson 5 - Project 1, Attempt 1
"""
This program stores the name and highest score of
each player.
"""

           
def high_score(shelf, player, score):
    # test existence of player in shelf
    if player in shelf.keys():
        # player exists; compare most recent score to existing and replace if greater
        if score > shelf[player]:
            shelf[player] = score
            
    else:
        # player doesn't exist so we'll add them to shelf
        shelf[player] = score
    # creating tuple of (player, score) so we can close shelf    
    player_score = (player, shelf[player])
    return player_score
        
    