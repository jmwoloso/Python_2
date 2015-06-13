#!/usr/bin/python3
#
# A Program That Tests the ClassFactory Function
#    testClassFactory.py
#
# Created by: Jason Wolosonovich
#    03-26-2015
#
# Lesson 11 - Project Attempt 1
"""
Testing module for the ClassFactory function.
"""

import unittest
from classFactory import build_row
import mysql.connector
from database_hw import login_info

class DBTest(unittest.TestCase):
    
    def setUp(self):
        """Create test database table and custom DataRow."""
        ### Test db table ###
        # connect to db
        self.db = mysql.connector.Connect(**login_info)
        # create cursor for db interaction
        self.cursor = self.db.cursor()
        # drop table if it exists
        self.cursor.execute("""DROP TABLE IF EXISTS animal_hw;""")
        # create animal table
        self.cursor.execute("""CREATE TABLE animal_hw(
                            id INTEGER PRIMARY KEY,
                            name VARCHAR(50),
                            family VARCHAR(50),
                            weight INTEGER);""")
        # animals we'll add to table
        self.animal_data = (
                   (1,
                    "Ellie", 
                    "Elephant", 
                    2350),
            
                    (10,
                     "Paul", 
                     "Python", 
                     150),
                            
                    (100,
                     "Ava",
                     "Dog",
                     75),
                            
                    (1000,
                     "Riley",
                     "Dog",
                     75)
                            
                    )
        # add animals to table
        self.cursor.execute("DELETE FROM animal_hw")
        for animal in self.animal_data:
            self.cursor.execute("""
            INSERT INTO animal_hw (id, name, family, weight)
            VALUES (%s, %s, %s, %s)""", animal)
        # commit db additions/changes
        self.db.commit()
        
        ### Test custom DataRow ###
        # create DataRow object
        A = build_row("animal_hw", "id name family weight")
        # create instance of DataRow class
        self.a = A([1, "Ellie", "Elephant", 2350])
        
    def test_attributes(self):
        # test for accuracy of instance attribute assignments
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.a.name, "Ellie")
        self.assertEqual(self.a.family, "Elephant")
        self.assertEqual(self.a.weight, 2350)
        """i = len(self.animal_data)
        ids, name, family, weight = zip(*self.animal_data)
        for e in range(i):
            self.assertEqual(ids[e], self.animal_data[e][0])
            self.assertEqual(name[e], self.animal_data[e][1])
            self.assertEqual(family[e], self.animal_data[e][2])
            self.assertEqual(weight[e], self.animal_data[e][3])"""
        
    def test_repr(self):
        "Tests repr method of DataRow class instance."""
        # make sure printed version is accurate
        self.assertEqual(repr(self.a),
                         "animal_hw_record(1, 'Ellie', 'Elephant', 2350)")
          
    def test_retrieve(self):
        """Tests retrive method of DataRow class instance."""
        B = build_row("animal_hw", "id name family weight")
        self.b = B([1, "Ellie", "Elephant", 2350])
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()
        self.condition = """SELECT name
                       FROM animal_hw
                       WHERE (animal_hw.id > 2);"""
        b = self.b.retrieve(self.cursor, self.condition)
        results = [info for info in b]
        self.assertEqual(results, [('Paul',),
                                   ('Ava',), 
                                   ('Riley',)
                                   ])       
    
    def tearDown(self):
        """Clean up function."""
        # remove food table
        self.cursor.execute("""DROP TABLE IF EXISTS animal_hw""")
        # terminate db connections
        self.db.close()

if __name__=="__main__":
    unittest.main()