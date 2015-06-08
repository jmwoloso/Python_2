#!/usr/bin/python3
#
# A Program to Create and Return Tailored Classes
#    classFactory.py
#
# Created by: Jason Wolosonovich
#    03-30-2015
#
# Lesson 11 - Project Attempt 2
"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows."""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        
        def __repr__(self):
            """defining repr method for class"""
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        
        def retrieve(self, curs, condition=None):
            """Generator to yield successive rows until result set is exhausted."""
            self.cursor = curs
            self.condition = condition
            self.cursor.execute("""SELECT name
                                   FROM animal_hw
                                   WHERE {0} {1} AND {2} {3}""".format(*condition))
            #stuff = self.cursor.fetchall()
            #for row in stuff:
            #    print(row)
            for row in self.cursor.fetchall():
                yield DataRow(row)
                   
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow