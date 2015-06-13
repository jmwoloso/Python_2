#!/usr/bin/python3
# A Program to Write and Read Lists to a File
#    fileops.py
#
# Created by: Jason Wolosonovich
#    02-23-2015
#
# Lesson 4 - Exercise 2
"""
Reads a list from a file and writes a list to a file.
"""

def write_list(fn, lst):
    """Writes a list to a named file. Each list item will be on
    a separate line. Overwrites the file if it already exists.
    """
    #with open(fn, "w") as f:
    #data = f.read()
    f = open(fn, "w")
    for item in lst:
        f.write("{0}\n".format(item))
    f.close()

def read_list(fn):
    """Reads a list from a file without using readline.
    Uses standard line endings ("\n") to delimit list items.
    """
    f = open(fn, 
             "r")
    s = f.read()
    f.close()
    # If the last character in the file is a newline, delete it
    if s[-1] == "\n":
        s = s[:-1]
    l = s.split("\n")
    return l
