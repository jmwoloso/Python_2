#!/usr/bin/python
#
# A Program That Verifies Every Animals Eats At Least One Food
#    animal_menu.py
#
# Created by: Jason Wolosonovich
#    03-19-2015
#
# Lesson 10 - Project Attempt 1
"""
Verifies that every animal eats at least one food.
"""

import mysql.connector
from database_hw import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

# select distinct number of animal ids (number of animals) in the food table
cursor.execute("""SELECT COUNT(DISTINCT anid) 
                  FROM food;""")
number_in_food_table = cursor.fetchone()[0]
# select distinct number of animal ids (number of animals) in the animal table
cursor.execute("""SELECT COUNT(id) 
                  FROM animal;""")
number_in_animal_table = cursor.fetchone()[0]
print("Unique animals in 'food' table: {0}".format(number_in_food_table))
print("Unique animals in 'animal' table: {0}".format(number_in_animal_table))

### ALTERNATE IMPLEMENTATION ###
#SELECT name, COUNT(feed)
#FROM food JOIN animal ON food.anid=animal.id
#GROUP BY anid;

cursor.execute("""SELECT name, COUNT(feed) 
                  FROM food JOIN animal ON food.anid=animal.id 
                  GROUP BY anid;""")
test = cursor.fetchall()
print("\nAnimal Name : Types of Food")
for name, count in test:
    print("{0} : {1}".format(name, 
                             count))
