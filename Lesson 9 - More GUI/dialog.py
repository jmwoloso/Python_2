#!/usr/bin/python3
#
# Sample Dialog Box in Tkinter
#    dialog.py
#
# Created by: Jason Wolosonovich
#    03-13-2015
#
# Lesson 9 - Exercise 4
"""
Demonstration of the simpledialog subclass of tkinter
"""
from tkinter import *
from tkinter.simpledialog import Dialog

class MyDialog(Dialog):
    """Create custom Dialog class."""
    def body(self, master):
        self.result = None
        for r in range(5):
            for c in range(5):
                b = Button(master, 
                           text="Row {0} Col {1}".format(r,
                                                         c))
                b.grid(row=r, 
                       column=c)
        print("Dialog created")
        
    def apply(self):
        self.result = "OK"
        
class Application(Frame):
    """Create main application window."""
    def create_dialog(self):
        d = MyDialog(self)
        print(d.result)
    
    def create_widgets(self):
        self.d_button = Button(self, 
                               text="Dialog...", 
                               command=self.create_dialog)
        self.d_button.pack({"side" : "left"})
        
        self.QUIT = Button(self, 
                           text="Quit", 
                           fg="red", 
                           command=self.quit)
        self.QUIT.pack({"side" : "left"})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
root = Tk()
app = Application(master=root)
app.mainloop()
        