"""Demonstrates unittest module in action"""
import unittest

#test code defining 's'
s = 'hello'

def title(s):
    '''Function to be used for testing'''
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]

class TestTitle(unittest.TestCase):
    
    def test_title_func(self):
        '''Tests effectiveness of 'title' function'''
        self.assertEqual(title(s), s.title(), "This function perfectly matches the str.title() method")

if __name__ == "__main__":
    unittest.main()