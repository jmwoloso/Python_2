#!/usr/bin/python
#
# A Program That Verifies Every Animals Eats At Least One Food
#    animal_menu.py
#
# Created by: Jason Wolosonovich
#    03-26-2015
#
# Lesson 10 - Project Attempt 3
"""
Verifies that every animal eats at least one food.
"""

import unittest
import mysql.connector
from database_hw import login_info

class TestMenu(unittest.TestCase):
    """Test case for animal database."""
    
    def setUp(self):
        """Create test database and tables."""
        # connect to db
        self.db = mysql.connector.Connect(**login_info)
        # create cursor for db interaction
        self.cursor = self.db.cursor()
        # drop table if it exists
        self.cursor.execute("""DROP TABLE IF EXISTS food_hw;""")
        self.cursor.execute("""DROP TABLE IF EXISTS animal_hw;""")
        # create animal table
        self.cursor.execute("""CREATE TABLE animal_hw(
                            id INTEGER PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(50),
                            family VARCHAR(50),
                            weight INTEGER);""")
        # animals we'll add to table
        self.animal_data = (
                   ("Ellie", 
                    "Elephant", 
                    2350),
            
                    ("Paul", 
                    "Python", 
                    150),
                            
                    )
        # add animals to table
        self.cursor.execute("DELETE FROM animal_hw")
        for animal in self.animal_data:
            self.cursor.execute("""
            INSERT INTO animal_hw (name, family, weight)
            VALUES (%s, %s, %s)""", animal)
        # commit db additions/changes
        self.db.commit()
        # drop table if it exists
        self.cursor.execute("""DROP TABLE IF EXISTS food_hw""")
        # create food table
        self.cursor.execute("""CREATE TABLE food_hw (
                            id INTEGER PRIMARY KEY AUTO_INCREMENT,
                            anid INTEGER,
                            feed VARCHAR(20),
                            FOREIGN KEY (anid) REFERENCES animal_hw(id))""")
        
        food_data = [('Ellie', 
                      'Elephant', 
                      ['hay', 
                       'peanuts']),
                
                     ('Paul', 
                      'Python', 
                      ['mice', 
                       'sql',
                       'data']),
                     
                     
                     ]
        # add food to table        
        for name, family, foods in food_data:
            self.cursor.execute("""SELECT id FROM animal_hw 
                                   WHERE name=%s and family=%s""",(name, 
                                                                   family))
            
            ids = self.cursor.fetchone()[0]
            for food in foods:
                self.cursor.execute("""INSERT INTO food_hw (anid, feed) 
                                       VALUES (%s, %s);""", (ids,
                                                             food))
        self.db.commit()
                    
    def test_hungry_animals(self):
        """Checks that all animals have food."""
        # select unique number of animals in food table
        self.cursor.execute("""SELECT COUNT(DISTINCT anid)
                               FROM food_hw;""")
        # object assignment for comparison
        number_in_food_table = self.cursor.fetchone()[0]
        # select unique animals in animal table
        self.cursor.execute("""SELECT COUNT(id)
                               FROM animal_hw;""")
        # object assignment for comparison
        number_in_animal_table = self.cursor.fetchone()[0]
        # capture hungry animals (if they exist)
        a = self.cursor.execute("""SELECT name, family
                               FROM animal_hw
                               WHERE animal_hw.id
                               NOT IN (
                                       SELECT anid FROM food_hw);""")
        # tuple of animal (name,family) in case animals share names
        hungry_animals = self.cursor.fetchall()
        # test for hungry animals
        self.assertEqual(number_in_food_table,
                         number_in_animal_table,
                         "\nOnly {0} out of {1} animals have food.\
                         \nGet food for:\n{2:}".format(number_in_food_table,
                                                              number_in_animal_table,
                                                              hungry_animals))
    
    def tearDown(self):
        """Removes temporary database tables."""
        # remove animal table
        self.cursor.execute("""DROP TABLE IF EXISTS food_hw""")
        # remove food table
        self.cursor.execute("""DROP TABLE IF EXISTS animal_hw""")
        # terminate db connections
        self.db.close()
        


if __name__=="__main__":
    unittest.main()
