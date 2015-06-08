#!/usr/bin/python3
#
# A Program Demonstrating the 'rowspan' and 'columnspan' Keywords
# for the grid() Method Geometry Manager in Tkinter
#
# Created by: Jason Wolosonovich
#   03-11-2015
#
# Lesson 8 - Exercise 3
"""
Demonstrates the 'rowspan' and 'columnspan' keywords of the
Geometry Manager for the grid() method.
"""
from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, 
                                 weight=1)
        self.master.columnconfigure(0, 
                                    weight=1)
        self.grid(sticky=ALL)
        for r in range(5):
            self.rowconfigure(r, 
                              weight=1)
            Button(self, 
                   text="Row {0}".format(r)).grid(row=r, 
                                                  column=0, 
                                                  sticky=ALL)
        self.rowconfigure(5, 
                          weight=1)
        for c in range(5):
            self.columnconfigure(c, 
                                 weight=1)
            Button(self, 
                   text="Col {0}".format(c)).grid(row=5, 
                                                  column=c, 
                                                  sticky=ALL)
        f = Frame(self, 
                  bg="red")
        f.grid(row=2, 
               column=1, 
               rowspan=3, 
               columnspan=2, 
               sticky=ALL)
        
root = Tk()
app = Application(master=root)
app.mainloop()
            