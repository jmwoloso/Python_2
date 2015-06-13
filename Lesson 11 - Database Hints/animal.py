#!/usr/bin/python3
#
# A Program That Uses a Class to Represent an Animal in the Database
#    animal.py
#
# Created by: Jason Wolosonovich
#    03-20-2015
#
# Lesson 11 - Exercise 2
"""
animal.py: a class to represent an animal in the database
"""

class Animal:
    
    def __init__(self, id, name, family, weight):
        self.id = id
        self.name = name
        self.family = family
        self.weight = weight
        
    def __repr__(self):
        return "Animal({0}, '{1}', '{2}', {3})".format(self.id,
                                                       self.name,
                                                       self.family,
                                                       self.weight)
        ### ALTERNATE VERSION ###
        # the code below selects the fields from within the actual format rather than
        # having to pass along a list of the variables to the format function
        # the '!r' syntax tells the interpreter to substitute the objects repr()
        # representation (that's why strings will be displayed with quotation
        # marks around them, even though none appear in the format
        # return "Animal({0.id!r}, {0.name!r}, {0.family!r}, {0.weight!r})".format(self)

if __name__=="__main__":
    import mysql.connector
    from database import login_info
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    cursor.execute("""SELECT id, name, family, weight
                      FROM animal""")
    animals = [Animal(*row)
               for row in cursor.fetchall()]
    from pprint import pprint
    pprint(animals)
    
    ### Tailored Class ###
    """A function that returns a tailored class"""
    # RC = RecordClass("animal", "id name family weight"))
    """Create instances of the class by calling the function with 
    values for each of the named columns."""
    # for row in cursor.fetchall():row_record = RC(*row))