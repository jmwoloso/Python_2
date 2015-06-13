#!/usr/bin/python3
#
# Program to Build a Window Layout
#    framer.py
#
# Created by: Jason Wolosonovich
#    03-12-2015
#
# Lesson 8 - Project Attempt 1
"""
Creates a window layout according to specifications
"""
from tkinter import *

class Application(Frame):
    """Creates the main application window."""
    
    def __init__(self, master=None):
        """Initialize the parent frame."""
        Frame.__init__(self, 
                       master, 
                       bg="white")
        self.master.rowconfigure(0, 
                                 weight=1)
        self.master.columnconfigure(0, 
                                    weight=1)
        self.master.title("Project 8 - Framer.py")
        self.grid(sticky=N+S+E+W)
        
        # configure main frame rows
        for r in range(2):
            self.rowconfigure(r, 
                              weight=1)
        # add buttons in the last row for each column
        for c in range(5):
            self.columnconfigure(c, 
                                 weight=1)
            Button(self, 
                   text="Button {0}".format(c+1), 
                   font=("Times New Roman", 8)).grid(row=2, 
                                                     column=c, 
                                                     sticky=S+W+E)
        self.createWidgets()
        
    def createWidgets(self):
        """Place widgets in application window."""
        
        # add frame 1
        self.f1 = Frame(self, 
                        bg="green")
        Label(self.f1, 
                text="Frame 1", 
                font=("Times New Roman", 8), 
                bg="green", 
                fg="black", 
                height=7, 
                width=24).pack(expand=True)
            
        self.f1.grid(row=0, 
                     column=0, 
                     rowspan=1, 
                     columnspan=2, 
                     sticky=N+S+W+E)
            
        # add frame 2
        self.f2 = Frame(self, 
                        bg="black")
        Label(self.f2, 
              text="Frame 2", 
              font=("Times New Roman", 8), 
              bg="black", 
              fg="white", 
              height=7, 
              width=24).pack(expand=True)
           
        self.f2.grid(row=1, 
                     column=0, 
                     rowspan=1, 
                     columnspan=2, 
                     sticky=N+S+W+E)
            
        # add frame 3
        self.f3 = Frame(self, 
                        bg="yellow")
        Label(self.f3, 
              text="Frame 3", 
              font=("Times New Roman", 8), 
              bg="yellow", 
              fg="black", 
              height=14, 
              width=36).pack(expand=True)
            
                        
        self.f3.grid(row=0, 
                     column=2, 
                     rowspan=2, 
                     columnspan=3, 
                     sticky=N+S+W+E)
        
                
root = Tk()
app = Application(master=root)
app.mainloop()       