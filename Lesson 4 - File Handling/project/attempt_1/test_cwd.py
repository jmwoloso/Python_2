#!/usr/bin/python3
#
# A Program That Tests the Current Working Directory Homework Assignment
#    test_cwd.py
#
# Created by: Jason Wolosonovich
#    02-24-2015
#
# Lesson 4 - Project 1, Attempt 1
"""
Tests the function within cwd.py and accesses the
file_suffix_dict within the suffix.py module
"""
import unittest
import os
import shutil
import cwd
from tempfile import mkdtemp, NamedTemporaryFile
from random import randint, sample
from suffix import file_suffix_dict
from collections import Counter


class TestExamineCWD(unittest.TestCase):
    """ Test case for functionality of current working directory function. """
    
    def setUp(self):
        """ This function runs before each test and creates temporary
        directories in addition to files with varying
        extensions. """
        # gather current working directory
        self.fixture_origdir = os.getcwd()
        # create temp directory for testing
        self.fixture_make_temporary_directory = mkdtemp("waiting_room")
        # set cwd to temporary directory
        os.chdir(self.fixture_make_temporary_directory)
        # create additional folders with file extensions in their name
        # to ensure robustness of testing
        self.fixture_temp_dir_1 = mkdtemp(suffix=".aaaaaa", prefix="ZZZZZZZZZZZZZZZZZ", dir=os.getcwd())
        self.fixture_temp_dir_2 = mkdtemp(suffix=".zzzzzz", prefix="AAAAAAAAAAAAAAAAA", dir=os.getcwd())
        
    def test_cwd_doctor(self):
        """Creates a random number of files with random file extensions
        for use in testing cwd_hw.py """
        # choose 'k' file extenstions randomly
        self.k_extensions = sample(list(file_suffix_dict.values()), 
                                  (randint(5, len(file_suffix_dict))))
        # create a file for each extension and append to temp_files
        temp_files = []
        for ext in self.k_extensions:
            i = 0
            number_of_files =  randint(1, 
                                       len(file_suffix_dict))
            while i < number_of_files + 1:
                f = NamedTemporaryFile(mode=r"w+b",
                                       suffix=ext,
                                       dir=os.getcwd(),
                                       delete=False)
                f.close()
                # append to list; no isfile() check needed, since we know it
                # was just created and is a file, not a folder, etc.
                temp_files.append(os.path.basename(f.name))
                i += 1
                
        # split name and extension; create list of extensions
        extensions = []
        for f in temp_files:
            name, extension = f.split(os.extsep, 1) # possible solution but cuts off leading '.'
            #name, extension = os.path.splitext(f)  # returns leading '.' but doesn't deal with double extensions
            extensions.append(extension)
        # use built-in Counter to return counts of each
        test_results = Counter(extensions)
        exam_results = cwd.doctor(os.getcwd())
        
        # in case of failure...
        msg=("\nTHESE COUNTS SHOULD BE THE SAME:\n"
             "cwd.doctor Counts: {0}\n"
             "True Counts: {1}\n".format(exam_results, test_results))
        
        self.assertEqual(test_results,
                         exam_results,
                         msg)
        
    
    def tearDown(self):
        """ This function runs after the tests are finished and deletes the temp
        directory and files created prior to running the tests. """
        # change back to original directory
        os.chdir(self.fixture_origdir)
        # delete temporary directory and files
        shutil.rmtree(self.fixture_make_temporary_directory)
        
if __name__ == "__main__":
    unittest.main()
    