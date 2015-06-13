#!/usr/bin/python3
#
# A Program Demonstrating Event Hanlding with Tkinter
#    clickreport.py
#
# Created by: Jason Wolosonovich
#   03-13-2015
#
# Lesson 9 - Exercise 1
"""
Demonstrates event handling with tkinter
"""
from tkinter import *

root = Tk()

def handler(event):
    print("clicked at", 
          event.x, 
          event.y)
    
frame = Frame(root, 
              width=100, 
              height=100)
frame.bind("<Button-1>", 
           handler)
frame.pack()

root.mainloop()