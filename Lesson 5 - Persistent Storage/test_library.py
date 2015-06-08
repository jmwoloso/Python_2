#!/usr/bin/python3
#
# A Program to Test Book Info Retrieval from a Persistent Data Source
#    test_library.py
#
# Created by: Jason Wolosonovich
#    02-26-2-15
#
# Lesson 5 - Exercise 2
"""
Demonstrates testing book info retrieval from a
persistent file store.
"""

import unittest
import library
import os
import glob

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """ Creating the library instance, authors and books by those
        authors, then adding them to the library for testing. """
        self.lib_fn = r"v:\workspace\PersistentStorage\src\lib.shelve"
        self.lib = library.Library(self.lib_fn)
        self.fixture_author1 = library.Author('Octavia',
                                              'Estelle',
                                              'Butler')
        self.fixture_book1 = library.Book('0807083100',
                                          'Kindred',
                                          [self.fixture_author1])
        self.fixture_author2 = library.Author('Robert',
                                              'Anson',
                                              'Heinlein')
        self.fixture_book2 = library.Book('0441790348',
                                          'Stranger in a Strange Land',
                                          [self.fixture_author2])
        self.lib.add(self.fixture_book1)
        self.lib.add(self.fixture_book2)
        
    def testGetByIsbn(self):
        """ Tests book retrieval by ISBN. """
        observed = self.lib.get_by_isbn(self.fixture_book1.isbn)
        self.assertEqual(observed,
                         self.fixture_book1)
        
    def testGetByTitle(self):
        """ Tests book retrieval by Title. """
        observed = self.lib.get_by_title(self.fixture_book2.title)
        self.assertEqual(observed,
                         self.fixture_book2)
        
    def testGetByAuthor(self):
        """ Tests retrieval by author. """
        observed = self.lib.get_by_author(self.fixture_book1.authors[0])
        self.assertEqual(observed, 
                         self.fixture_book1)
        
    def tearDown(self):
        """ Cleanup time. """
        self.lib.close()
        shelve_files = glob.glob(self.lib_fn + '*')
        for fn in shelve_files:
            os.remove(fn)
            
if __name__ == "__main__":
    unittest.main()