#!/usr/bin/python3
#  A Program to Join Path and Filenames for Return to test_latest Program
#    latest.py (formerly latest2.py from Lesson 4)
#
# Created by: Jason Wolosonovich
#    03-05-2015
#
# Lesson 6 - Exercise 1
"""
Takes file name and directory input from test_ziplatest.py
and joins them together returning the result for use in
the tests. This has the added feature of using list 
comprehensions if desired via the LIST_COMP toggle.
Updated for Lesson 6 - Exercise 1
"""
import glob
import os
import zipfile

def latest(num=1, path=".", LIST_COMP=False):
    # 1. original data
    files = glob.glob(os.path.join(path, 
                                   "*"))
    if LIST_COMP:
        """"
        Demonstration of decorate-sort-undecorate functionality
        within list comps; dates are not required but are added
        because Python sorts these easily and in ascending order
        by default so more recent files are located at the end
        """
        # 2. original data decorated with file creation times
        dated_files = [(os.path.getmtime(fn), 
                        os.path.abspath(fn)) 
                        for fn in files]
        # 3. decorated data sorted in decorator order
        dated_files.sort()
        # 4. sorted in decorator order with decorators removed
        latest_files = [f for (d,f) 
                        in dated_files[-num:]]
        latest_files.reverse()
        return latest_files
    else:
        files_with_dates = []
        latest_files = []
        for fn in files:
            files_with_dates.append((os.path.getmtime(fn), 
                                     os.path.abspath(fn)))
        files_with_dates.sort()
        """
        Extracts just the filenames of the most recent files by using the
        negative index located in this chunk of code. -num makes it go
        backwards through the values of num, then reverses the result, putting
        the most recent files at the beginning. (i.e. moves backwards from the
        end of the list)
        """
        for file_info in files_with_dates[-num:]:
            latest_files.append(file_info[1])
    
    # 5. reversed to give "most recent first" as natural order     
    latest_files.reverse()
    return latest_files

def zip_latest(fn, num, path):
    files_to_archive = latest(num, 
                              path)
    zf = zipfile.ZipFile(fn, 
                         "w", 
                         zipfile.ZIP_DEFLATED)
    for fn_to_archive in files_to_archive:
        zf.write(fn_to_archive)
    zf.close()