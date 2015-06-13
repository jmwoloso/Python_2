#!/usr/bin/python
#
# Test Suite for gone_fishin.py
#     testGoneFishin.py
#
# Created by: Jason Wolosonovich
#    05-12-2015
#
# Lesson 13 - Project Attempt 1
import unittest
import time
import mysql.connector
from database import login_info
from datetime import datetime
from gone_fishin import generate_messages, save_to_db, send_to_console


# table definition for testing
TBLDEF = """CREATE TABLE jotd_emails(
            msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
            msgMessageID VARCHAR(128),
            msgDate DATETIME,
            msgSenderName VARCHAR(128),
            msgSenderAddress VARCHAR(128),
            msgSenderSubject VARCHAR(128),
            msgText LONGTEXT)"""

# we want to test different lengths of time
DAYCOUNT = [1,10,50,100,500]

# send emails to these folks
RECIPIENTS = [('Pat Barton', 'learn@oreilly.com'),
              ('Jason Wolosonovich', 'jmwoloso@asu.edu')]

# Date to start sending generated jotd emails
STARTTIME = datetime.date(datetime.strptime('07/04/2015', '%m/%d/%Y'))
# email subject line
subject = "Jason's Joke of the Day"
# person sending the email
sender = '<a href="mailto:jmwoloso@asu.edu">jmwoloso@asu.edu</a>'        
# message content
text = """A pirate walks into a bar with a ship's steering wheel hanging from his
crotch:

Bartender: "What the hell is that?"
Pirate: "I don't know but it's drivin' me nuts!" """ 

# name of db table to create
table = 'jotd_emails'



class TestGoneFishin(unittest.TestCase):
    """
    Testing suite for gone_fishin.py. 
    
    CAUTION: This test suite will delete any
    existing tables with the same name.
    """
    def setUp(self):
        """
        Setup for testing environment.
        """
        # establish db connection
        # initialize db connection and cursor for table access
        self.connection = mysql.connector.Connect(**login_info)
        self.cursor = self.connection.cursor()
        # prepare the database table for testing
        self.cursor.execute("""DROP TABLE IF EXISTS jotd_emails""")
        # avoid metadata lock
        self.connection.commit()
        # create messages table
        self.cursor.execute(TBLDEF)
        # avoid metadata lock
        self.connection.commit()
                   
    
    def test_creation_times(self):    
        """
        Displays the time taken during message generation.
        """
        # container for message generation speed
        self.msgs_per_second = []
        # container for message generation times
        self.timing_list = []
        # loop through values in DAYCOUNT and time them
        for DAYS in DAYCOUNT:
            # time for later testing
            self.start = time.time()
            self.message_dict = generate_messages(RECIPIENTS, 
                                                  STARTTIME, 
                                                  DAYS,
                                                  text,
                                                  subject,
                                                  sender)
            self.end = time.time()
            # add the tuple to our timing list
            self.timing_list.append(("DAYCOUNT={0}".format(DAYS), self.end - self.start))
        
        # time to see how we did (ha!)
        print("\n#### TIMING RESULTS ####")
        for i in range(0, len(self.timing_list)):
            print("{0} --> {1} seconds".format(self.timing_list[i][0], self.timing_list[i][1]))
            self.msgs_per_second.append(DAYCOUNT[i] / self.timing_list[i][1])
        
        print("\n\n#### MESSAGE GENERATION TIMES ####")
        for i, DAYS in enumerate(DAYCOUNT):
            print("Messages per Second: {0}".format(self.msgs_per_second[i]))
            print("Number of Messages: {0}".format(DAYS))
            print("Time to Generate: {0} seconds\n".format(self.timing_list[i][1]))
                             
                     
    def test_generate_messages(self):
        """
        Tests generate_messages function from gone_fishin.py.
        """
        # run through generating emails for all values in DAYCOUNT
        for DAYS in DAYCOUNT:
            self.message_dict = generate_messages(RECIPIENTS, 
                                                  STARTTIME, 
                                                  DAYS,
                                                  text,
                                                  subject,
                                                  sender)
        # test if messages were generated
        self.assertGreater(len(self.message_dict),
                           0,
                           "No messages generated!")
        
               
    def test_send_to_console(self):
        """
        Tests the send_to_console printing function of
        gone_fishin.py. Pseudo-check for correct message
        format.
        """
        for DAYS in DAYCOUNT:
            self.message_dict = generate_messages(RECIPIENTS, 
                                                  STARTTIME, 
                                                  DAYS,
                                                  text,
                                                  subject,
                                                  sender)
        send_to_console(self.message_dict)
        # check that we have all headers
        # we specified when the messages were created
        for k,v in self.message_dict.items():
            self.assertTrue(v[0]['date'], 
                            "Messages have no dates!")
            self.assertTrue(v[0]['from'],
                            "Messages have no sender!")
            self.assertTrue(v[0]['to'],
                            "Messages have no recipient!")
            self.assertTrue(v[0]['subject'],
                            "Messages have no subject!")
            self.assertTrue(v[0]['message-id'],
                            "Messages have no message-id!")
            self.assertGreater(len(v[0].get_payload()),
                               0,
                               "Messages have no content!")
            
     
    def test_save_to_db(self):
        """
        Tests the mechanism to save generated messages to db table.
        """
        # run through generating emails for all values of DAYCOUNT
        for DAYS in DAYCOUNT:
            self.message_dict = generate_messages(RECIPIENTS, 
                                                  STARTTIME, 
                                                  DAYS,
                                                  text,
                                                  subject,
                                                  sender)
                        
            # save messages to db table
            save_to_db(self.message_dict, login_info, table)
        # query the number of emails in the db table
        self.cursor.execute("""SELECT COUNT(*) FROM jotd_emails""")
        # save result of query
        self.count_stored = self.cursor.fetchone()[0]
        # avoid metadata lock
        self.connection.commit()
        # make sure the correct number were saved
        self.assertEqual(self.count_stored,
                         sum(DAYCOUNT)*len(RECIPIENTS),
                         "Something isn't adding up!")
           
          
if __name__=="__main__":
    unittest.main()    