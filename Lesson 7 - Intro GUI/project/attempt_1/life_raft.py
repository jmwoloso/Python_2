#!/usr/bin/python3
#
# A GUI to Convert (If Possible) Two Entries to Type(Float)
#    life_raft.py
#
# Created by: Jason Wolosonovich
#   03-10-2015
#
# Lesson 7 - Project Attempt 1
"""
Takes the values of two GUI entry fields and attempts
to convert them to float values.
"""
from tkinter import *
from urllib.request import urlopen
import base64


class Application(Frame):
    """ Application main window class. """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def click_callback(self, event):
        """ Erases widget contents (the first time) based on which entry 
            field has been selected."""
        if event.widget == self.entry_1:
            self.entry_1.delete(0, 
                                END)
            self.entry_1.config(fg='black')
               
        elif event.widget == self.entry_2:
            self.entry_2.delete(0, 
                                END)
            self.entry_2.config(fg='black')
    
    def tab_callback(self, event):
        """Erases widget contents (the first time) based on a given entry
           field being navigated to via the <TAB> button."""
        if event.widget == self.button:
            if self.entry_1['fg'] == 'black':
                pass
            else:
                self.entry_1.delete(0, 
                                    END)
                self.entry_1.config(fg='black')
            
        elif event.widget == self.entry_1:
            if self.entry_2['fg'] == 'black':
                pass
            else:
                self.entry_2.delete(0, 
                                    END)
                self.entry_2.config(fg='black')
            
        
    def createWidgets(self):
        """ Add the entry fields, button and label
        widgets to the main Frame in the GUI. """
        # get python logo and convert for use
        self.url = "https://wiki.gogrid.com/images/0/0f/Python.gif"
        self.image_bytes = urlopen(self.url).read()
        self.image = base64.encodebytes(self.image_bytes)
        self.photo = PhotoImage(data=self.image)
        # add logo to label widget
        self.logo = Label(self,
                          image=self.photo).pack()
        
        # create another label widget
        self.label = Label(self, 
                           text="Enter Two Values",
                           font=("Verdana", 26, "bold"))
        self.label.pack(side=TOP)
            
        # create entry widget
        self.entry_1 = Entry(self, 
                             font=("Fixedsys", 18, "italic"), 
                             fg='light gray')
        self.entry_1.bind("<Button-1>", 
                          self.click_callback)
        self.entry_1.bind("<Tab>", 
                          self.tab_callback)
        self.entry_1.insert(0, 
                            "Value 1")  
        self.entry_1.pack()                   
                
        # create another entry widget
        self.entry_2 = Entry(self, 
                             font=("Fixedsys", 18, "italic"), 
                             fg='light gray')
        self.entry_2.bind("<Button-1>", 
                          self.click_callback)
        self.entry_2.insert(0, 
                            "Value 2")
        self.entry_2.pack()
        
        # create button widget
        self.button = Button(self, 
                             text="Convert",
                             font=("Verdana", 16, "bold"), 
                             command=self.handler)
        self.button.bind("<Tab>", 
                         self.tab_callback)
        self.button.pack()
                
        
    def handler(self):
        """ Attempts to convert entry values to type float."""
        try:
            e1 = self.entry_1.get()
            e2 = self.entry_2.get()
            answer = float(e1) + float(e2)
            
        except ValueError:
            val_error = "***ERROR***"
            return self.label.config(text=val_error)
        
        self.label.config(text=answer)
    
      
root = Tk()
app = Application(master=root)
app.mainloop()
    