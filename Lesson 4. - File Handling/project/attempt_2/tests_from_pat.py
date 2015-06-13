#!/usr/bin/python3
# Tests from Pat

import unittest
import os
from tempfile import mkdtemp
import shutil
import cwd

class TestModule(unittest.TestCase):
       
    def setUp(self):
        self.home = os.getcwd()
        self.testdir = mkdtemp()
        os.chdir(self.testdir)

    def test_working(self):
        for file in ["test1.doc", 
                     "test2.doc", 
                     "long.file.ext.tz", 
                     "no_ext", 
                     "joe.zip"]:
            f = open(file, 'w').close()  
        expected = {".doc":2, ".tz":1, "":1, ".zip":1}  # dict of expected extensions        
        observed = cwd.doctor(os.getcwd())
        print(expected)
        print(observed)
        self.assertEqual(observed, expected, "uh oh, problem")
        
    def tearDown(self):
        os.chdir(self.home)
        shutil.rmtree(self.testdir)
        
if __name__ == "__main__":
    unittest.main()
