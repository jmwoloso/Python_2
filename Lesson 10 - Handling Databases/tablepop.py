#!/usr/bin/python3
#
# A Program to Connect to a MySQL DB and Insert Data
#    tablepop.py
#
# Created by: Jason Wolosonovich
#    03-19-2015
#
# Lesson 10 - Exercise 1
"""
Populates a table with data from a Python tuple. 
"""
import mysql.connector
from database import login_info

if __name__=="__main__":
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    # create the table
    cursor.execute("""DROP TABLE IF EXISTS animal;""")
    cursor.execute("""CREATE TABLE animal(
                      id INTEGER PRIMARY KEY AUTO_INCREMENT,
                      name VARCHAR(50),
                      family VARCHAR(50),
                      weight INTEGER);""")
    data = (
            ("Ellie", 
             "Elephant", 
             2350),
            
            ("Gerald", 
             "Gnu", 
             1400),
            
            ("Gerald", 
             "Giraffe", 
             940),
            
            ("Leonard", 
             "Leopard", 
             280),
            
            ("Sam", 
             "Snake", 
             24),
            
            ("Steve", 
             "Snake", 
             35),
            
            ("Zorro", 
             "Zebra", 
             340)
            )
    
    cursor.execute("DELETE FROM animal")
    for t in data:
        cursor.execute("""
        INSERT INTO animal (name, family, weight)
        VALUES (%s, %s, %s)""", t)
    
    db.commit()
    print("Finished")
    