#!/usr/bin/python3
#
# Program to Build a Window Layout
#    framer_maxx.py
#
# Created by: Jason Wolosonovich
#    03-15-2015
#
# Lesson 9 - Project Attempt 1
"""
Creates a window layout according to specifications and adds functionality
"""
from tkinter import *
from random import randint
from glob import glob
import os




class Application(Frame):
    """Creates the main application window."""
    
    ### CLASS DEFINITION ###      
    def __init__(self, master=None):
        """Initialize the parent frame."""
        Frame.__init__(self, 
                       master, 
                       bg="white")
                       
        # configure master window
        self.master.rowconfigure(0,
                                 weight=1)
        
        self.master.columnconfigure(0,
                                    weight=1)
        
        self.master.title("Project 9 - framer_maxx.py")
        
        # configure geometry manager for class instance
        self.pack(fill="both", 
                  expand=True)#grid(sticky=N+S+W+E)
             
        # configuring rows and columns for frames
        for i in range(4):
            self.rowconfigure(i, 
                              weight=1)
        for j in range(5):
            self.columnconfigure(j,
                                 weight=1)
        self.createWidgets()
    
    ### HANDLER FUNCTIONS ###
    def click_handler(self, event):
        """Defines handling of click events in Frames 1 & 2, respectively."""
        print("{0} clicked at: {1},{2}".format(str(event.widget)
                                               .title()
                                               .split('.')[2], 
                                               event.x, 
                                               event.y))
        
    def color_handler(self, color):
        """Changes text color in Frame 3 Text widget."""
        self.t3["foreground"] = color
                
    def file_handler(self, *event):
        """Opens the file name specified in the Frame 3 Entry widget."""
        # get text info from entry widget
        # doesn't differentiate capitalization with file names and 
        # extensions???
        fname = self.e3.get()
        self.t3.delete("1.0", 
                       END)
        try:
            fname = self.e3.get()
            f = open(fname)
            self.t3.delete("1.0",
                           END)
            self.t3.insert("1.0", 
                           f.read())
            
        except FileNotFoundError:
            # change color of message with same entry value so user knows
            # the program is responding
            colors = ["red", 
                      "yellow", 
                      "green", 
                      "magenta", 
                      "orange", 
                      "cyan"]
            r = randint(0,5)
            if fname == "":
                self.t3.insert("0.0",
                               "You didn't enter a file name...try again\n")
                self.color_handler(colors[r])
                
            # equivalent to non-existent file    
            elif fname != "":
                self.t3.insert("0.0",
                               "The file you requested does not " + \
                               "exist in this directory...try again\n")
                self.e3.delete(0,
                               END)
                self.color_handler(colors[r])

                
    ### PLACE WIDGETS ON THE APP ###
    def createWidgets(self):
        """Place the widgets in the application window."""
            
        ### ADD FRAME 1 ###
        self.f1 = Frame(self,
                        bd=0, 
                        bg="green",
                        name="frame 1",
                        height=100,
                        width=150)
        # add label
        self.l1 = Label(self.f1,
                        text="Frame 1", 
                        font=("Times New Roman", 8), 
                        bg="green", 
                        fg="black", 
                        height=7, 
                        width=24)
        
        self.l1.bind("<Button-1>", 
                     self.click_handler)
        
        self.l1.pack(fill="both", 
                     expand=True)
        # configure layout
        self.f1.rowconfigure(0, 
                             weight=1)
        
        self.f1.columnconfigure(0, 
                                weight=1)
        
        self.f1.grid(row=0, 
                     column=0,  
                     rowspan=2,
                     columnspan=2, 
                     sticky=N+S+W+E)
                        
        ### ADD FRAME 2 ###
        self.f2 = Frame(self,
                        bd=0, 
                        bg="black",
                        name="frame 2",
                        height=100,
                        width=150)
        # add label
        self.l2 = Label(self.f2, 
                        text="Frame 2", 
                        font=("Times New Roman", 8), 
                        bg="black", 
                        fg="white", 
                        height=7, 
                        width=24)
        
        self.l2.bind("<Button-1>", 
                     self.click_handler)
        
        self.l2.pack(fill="both", 
                     expand=True)
        # configure layout
        self.f2.rowconfigure(0, 
                             weight=1)
        
        self.f2.columnconfigure(0, 
                                weight=1)
        
        self.f2.grid(row=2,
                     column=0,
                     rowspan=2,
                     columnspan=2,
                     sticky=N+S+W+E)
        
                
        ### ADD FRAME 3 ###
        self.f3 = Frame(self,
                        bd=0, 
                        bg="yellow",
                        name="frame 3",
                        height=200,
                        width=225)
        # add widgets to frame
        self.t3 = Text(self.f3, 
                       height=20, 
                       width=20)
        self.t3.grid(row=0, 
                     column=0, 
                     rowspan=5, 
                     columnspan=3, 
                     sticky=N+S+W+E)
        
        self.e3 = Entry(self.f3, 
                        width=20)
        
        # handle <ENTER> after file name is typed
        self.e3.bind("<Return>", 
                     self.file_handler)
        self.e3.grid(row=5, 
                     column=0, 
                     columnspan=3, 
                     sticky=S+W+E)
        
        # configure layout
        for i in range(5):
            self.f3.rowconfigure(i, 
                                 weight=1)
        for j in range(3):
            self.f3.columnconfigure(j, 
                                    weight=1)
        
        self.f3.grid(row=0,
                     column=2,
                     rowspan=4, 
                     columnspan=3, 
                     sticky=N+S+W+E)
        
        
        ### ADD FRAME 4 ###
        self.f4 = Frame(self,
                        bd=0,
                        name="frame 4")
        # configure layout
        self.f4.rowconfigure(0, 
                             weight=1)
        
        for j in range(5):
            self.f4.columnconfigure(j,
                                    weight=1)
        # add buttons
        self.b4_red = Button(self.f4,
                             name="red",
                             width=1,
                             text="Red",
                             font=("Times New Roman", 8),
                             command=lambda: self.color_handler("red"))
                
        self.b4_red.grid(row=0,
                         column=0,
                         columnspan=1,
                         sticky=S+W+E)
        
        self.b4_blue = Button(self.f4,
                              name="blue",
                              width=1,
                              text="Blue",
                              font=("Times New Roman", 8),
                              command=lambda: self.color_handler("blue"))
        
        self.b4_blue.grid(row=0,
                          column=1,
                          columnspan=1,
                          sticky=S+W+E)
        
        self.b4_green = Button(self.f4,
                               name="green",
                               width=1,
                               text="Green",
                               font=("Times New Roman", 8),
                               command=lambda: self.color_handler("green"))
        
        self.b4_green.grid(row=0,
                           column=2,
                           columnspan=1,
                           sticky=S+W+E)
        
        self.b4_black = Button(self.f4,
                               name="black",
                               width=1,
                               text="Black",
                               font=("Times New Roman", 8),
                               comman=lambda: self.color_handler("black"))
                
        self.b4_black.grid(row=0,
                           column=3,
                           columnspan=1,
                           sticky=S+W+E)
        
        self.b4_open = Button(self.f4,
                              name="open",
                              width=1,
                              text="Open",
                              font=("Times New Roman", 8),
                              command=self.file_handler)
        
        self.b4_open.grid(row=0,
                          column=4,
                          columnspan=1,
                          sticky=S+W+E)
            
        self.f4.grid(row=5, 
                     column=0,
                     columnspan=5, 
                     sticky=S+W+E) 
        
              
root = Tk()
app = Application(master=root)
app.mainloop()       