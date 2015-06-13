#!/usr/bin/python3
#
# A Program Demonstrating Geometry Manager for the pack() Method in Tkinter
#    sidebyside.py
#
# Created by: Jason Wolosonovich
#   03-11-2015
#
# Lesson 8 - Exercise 1
"""
Demonstrates the features of the pack() method's Geometry Manager.
"""
from tkinter import *

root = Tk()

w = Label(root, 
          text="Red Label", 
          bg="red", 
          fg="white")
# 'fill' occurs in the direction that the widgets aren't stacked in
w.pack(side=TOP, 
       fill=BOTH)
# 'expand' allows the widgets to fill the space of their parent along
# all dimensions
w = Label(root, 
          text="Green Label", 
          bg="green", 
          fg="black")
w.pack(side=TOP, 
       fill=BOTH, 
       expand=True)
w = Label(root, 
          text="Blue Label", 
          bg="blue", 
          fg="white")
w.pack(side=TOP, 
       fill=BOTH, 
       expand=True)

mainloop()