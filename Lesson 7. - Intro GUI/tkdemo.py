#!/usr/bin/python3
#
# A Program Demonstrating the tkinter Module
#    tkdemo.py
#
# Created by: Jason Wolosonovich
#    03-07-2015
#
# Lesson 7 - Exercise 1
"""
Demonstrating the tkinter module.
"""

from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("Hi there, everyone!")
        
    def createWidgets(self):
        # alternate syntax that would work, no need to save a reference
        # to the button since it is not called anywhere else in the code
        # Button(self, text="Hello", fg="blue", command=self.say_hi).pack(side="left")
        self.hi_there = Button(self, 
                               text="Hello", 
                               fg="blue", 
                               command=self.say_hi)
        self.hi_there.pack({"side" : "left"})
        # Button(self, text="Goodbye", fg="red", command=self.quit).pack(side="left")
        self.QUIT = Button(self, 
                           text="Goodbye", 
                           fg="red", 
                           command=self.quit)
        self.QUIT.pack({"side" : "left"})
        
        
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
root = Tk()
app = Application(master=root)
app.mainloop()
        