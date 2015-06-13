#!/usr/bin/python3
#
# A Program to Implement a Simple Database Record Class
#    datarow.py
#
# Created by: Jason Wolosonovich
#    03-20-2015
#
# Lesson 11 - Exercise 3
"""
datarow.py: implements a simple databse record class
"""

class row:
    def __init__(self, cols, data):
        self.__dict__.update(zip(cols, data))
    def __repr__(self):
        return "user_record(id={0.id} name={0.name} email={0.email})".format(self)
    
if __name__=="__main__":
    r1 = row(['id', 'name', 'email'],
             (1, "Steve Holden", "steve@holdenweb.com"))
    if r1.id != 1 or r1.name != "Steve Holden" or r1.email != "steve@holdenweb.com":
        print("TEST FAILED: id={0.id} name={0.name} email={0.email}".format(r1))