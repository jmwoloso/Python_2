#!/usr/bin/python3
#
# A Program to Archive Directories from a Given Path
#    arc_path.py
#
# Created by: Jason Wolosonovich
#    03-06-2015
#
# Lesson 6 - Project Attempt 1
"""
Takes a directory path and creates an archive of the directory only.
"""
import os
import zipfile
from glob import glob


def arc_path(path, archive):
    """ Examines cwd and creates a zipfile archive of the
    files (excluding subdirectories) within the directory. """
    # up one directory level so zip isn't in the directory
    # that it is archiving
    os.chdir(r"../")
    # open zipfile for writing
    zf = zipfile.ZipFile(archive, 
                         "w")
    # list of files in the directory
    files = glob(os.path.join(path, 
                              "*"))
    # write each file to the archive
    [zf.write(f) 
     for f in files 
     if os.path.isfile(f)]
    # populate list for return to test suite
    namelist = [os.path.join(os.path.basename(path), 
                             os.path.basename(f)) 
                             for f in zf.namelist()]
    # close the archive
    zf.close()
    return namelist