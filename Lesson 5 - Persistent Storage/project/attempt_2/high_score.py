#!/usr/bin/python3
#
# A Program to Keep Track of High Scores by Player
#    high_score.py
#
# Created by: Jason Wolosonovich
#    02-26-2015
#
# Lesson 5 - Project 1, Attempt 2
"""
This program stores the name and highest score of
each player.
"""
import shelve
           
def high_score(player, score):
    """ Function to record the player's number of zombie kills. """
    # create shelf
    shelf = shelve.open("walking_dead.shlf", writeback=True)
    # test if score can be turned to int    
    try:
        score = int(score)
        
    except ValueError:
        # value can't be converted; let user know
        player_score = "NaN: Not a valid score"
        return player_score
    
    # if score can be converted to valid number, continue
    # test existence of player in shelf
    if player in shelf.keys():
        # if new score > current score, replace
        if score > shelf[player]:
            shelf[player] = score
    else:
        # player doesn't exist so we'll add them to shelf
        shelf[player] = score
    # get player's highes score
    player_score = (shelf[player])
    # close the shelf
    shelf.close()
    # send high score back
    return player_score
        
    