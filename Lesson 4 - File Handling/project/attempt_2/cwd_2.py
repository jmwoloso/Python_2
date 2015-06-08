#!/usr/bin/python3
#
# A Program That Examins the Contents of the Current Working Directory
#    cwd_2.py
#
# Created by: Jason Wolosonovich
#    02-24-2015
#
# Lesson 4 - Project 1, Attempt 2
"""
This program examines the contents of the current working
directory and keeps a count of each type of file extension
within the directory
"""

import os
from collections import Counter

def doctor(cwd):
    """ Inspects the current directory and keeps a count of
    how many files have each unique extension type. """
    # set current working directory to value passed during function call
    os.chdir(cwd)
    
    
    # verifies items added are only files and not folders
    #files_in_cwd = [f for f in glob('*.*') if os.path.isfile(f)]
    extensions = []
    for f in os.listdir(os.getcwd()):
        if os.path.isfile(f):
            name, extension = os.path.splitext(f)  # returns leading '.' but doesn't deal with double extensions
            extensions.append(extension)
    # use built-in Counter to return counts of each
    exam_results = Counter(extensions)
    return exam_results