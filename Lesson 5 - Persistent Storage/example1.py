#!/usr/bin/python3
#
# A Program to Demonstrate Importing a Class from a Module
# Using Pickle
#    example1.py
#
# Created by: Jason Wolosonovich
#    02-26-2015
#
# Lesson 5 - Exercise 1
"""
Demonstrates how to import a Class from an external
module once we unpickle an instance of that class
"""

class Example:
    def __init__(self):
        self.item1 = None
    def item2(self):
        return "instance variable item 1 is {0}".format(self.item1)
