#!/usr/bin/python3
#
# Final Project: A Program That Stores Emails To Be Sent At A Later Date
#    gone_fishin.py
#
# Created by: Jason Wolosonovich
#    05-12-2015
#
# Lesson 13 - Project Attempt 1
"""
This program saves messages to be sent (at a later date)
in a database table
"""
import mysql.connector
from database import login_info
from settings import RECIPIENTS, STARTTIME, DAYCOUNT
from datetime import timedelta, date
from email.utils import make_msgid
from email.message import Message



def check_please(login_info=None, database=None, table=None):
    """
    Checks to see if the specified table exists.
    """
    # there may be more elegant methods, but this
    # is clean, simple to understand and gets the job done
    sql = """SELECT COUNT(*)
             FROM information_schema.tables
             WHERE table_schema='{0}'
             AND table_name='{1}'
             LIMIT 1;""".format(database, 
                                table)
    
    # login connection to db
    connection = mysql.connector.Connect(**login_info)
    # get pipeline for queries
    cursor = connection.cursor()
    # run query
    cursor.execute(sql)
    # save results
    does_exist = cursor.fetchone()[0]
    # always commit to prevent metadata lock
    connection.commit()
    
    return does_exist


def set_table(login_info=None, TBLDEF=None, table=None):
    """
    Creates the specified database table if it doesn't exist currently.
    """
    connection = mysql.connector.Connect(**login_info)
    cursor = connection.cursor()
    cursor.execute(TBLDEF)
    connection.commit()
    
        
def send_to_console(message_dict=None):
    """
    Print the results of generate_messages to the console,
    check formatting after print.
    """
    # print one day's worth of emails to verify formatting is
    # correct
    print("\n#### MESSAGE FORMAT DEMO #############################\n")
    for k,v in message_dict.items():
        
        # just printing the respective headers and doing
        # little bit of aesthetic formatting to make it
        # human-readable
        print("Date: {0}".format(v[0]['Date']))
        print("From: {0}".format(v[0]['From']))
        print("To: {0}".format(v[0]['To']))
        print("Subject: {0}".format(v[0]['Subject']))
        print("Message-Id: {0}".format(v[0]['Message-Id']))
        # payload is an apt word, these jokes are
        # histerical!
        print("\n{0}\n\n".format(v[0].get_payload()))
        print("#### END MESSAGE FORMAT DEMO #######################\n")
        break        
            
def save_to_db(message_dict=None, login_info=None, table=None):
    """
    Parses and saves the generated messages to the specified MySQL
    db table for storage.
    """
    # open db connection and create cursor object
    connection = mysql.connector.Connect(**login_info)
    cursor = connection.cursor()
    
    # take messages and insert into db table for storage
    for date in message_dict:
        for message in message_dict[date]:
            # grab message-id
            message_id = message['message-id']
            # grab date
            date = message['date']
            # grab sender
            sender = message['from']
            # grab recipient
            recipient = message['to']
            # grab subjeect line
            subject = message['subject']
            # grab the joke
            text = message['text']
            # query that will add all the info to db table
            sql = """INSERT INTO {0}(
                           msgMessageID, 
                           msgDate, 
                           msgSenderName,
                           msgSenderAddress, 
                           msgSenderSubject,
                           msgText) 
                           VALUES (%s, 
                                   %s, 
                                   %s, 
                                   %s, 
                                   %s, 
                                   %s)""".format(table)
            # these guys replace our string place holders in the
            # query above
            params = (message_id,
                      date,
                      sender,
                      recipient,
                      subject,
                      text)
            # run the query
            cursor.execute(sql, params)
            # avoid metadata lock
            connection.commit()
    

def generate_messages(RECIPIENTS=None, STARTTIME=None, DAYCOUNT=None, text=None, subject=None, sender=None):
    """
    Generates messages using the information contained in
    RECIPIENTS, STARTTIME, DAYCOUNT from the settings.py
    module.
    """
    # we'll store our created messages in this dict
    # until it's time to commit them to the db
    message_dict = {} 
    # generate emails using DAYCOUNT list
    # generate emails for DAY days
    for i in range(0, DAYCOUNT):
        # this will hold one day's emails at a time
        message_list = []
        # we need one email per recipient for each of the DAY days
        for j in range(0, len(RECIPIENTS)):
            # create one message
            message = Message()
            # add 'date' header
            message['Date'] = STARTTIME.strftime('%m/%d/%Y')
            # add sender's address 
            message['From'] = sender
            # add the recipient's name and email addy
            message['To'] = "{0} <{1}>".format(RECIPIENTS[j][0],
                                               RECIPIENTS[j][1])
            # add subject line for the message 
            message['Subject'] = subject + \
                                 " for {0}!".format(STARTTIME.strftime('%m/%d/%Y'))
            # since we're not actually sending these, we still want the
            # unique message-id for the db table and for sending later   
            message['Message-Id'] = make_msgid()
            # add joke of the day
            message.set_payload(text)
            # add this message to the days list of messages
            message_list.append(message)
        # add each message list to a dict where the key is the string repr
        # of STARTTIME and the values is the message_list containing all
        # the emails to be sent on that particular day
        message_dict[STARTTIME.strftime('%m/%d/%Y')] = message_list
        # increment STARTTIME by one day and do it all over again
        STARTTIME += timedelta(days=1)
                    
    return message_dict


def main():
    """
    main loop for running script
    """
    #### USER INPUT NEEDED HERE #####################################
    # ensure db table exists before generating
    # and saving messages
    database = 'jwoloson' # database you wish to save messages in
    table = 'jotd_emails' # name of the db table you're saving to
    # database table definition (if needed)
    TBLDEF = """\
    CREATE TABLE {0}(
         msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
         msgMessageID VARCHAR(128),
         msgDate DATETIME,
         msgSenderName VARCHAR(128),
         msgSenderAddress VARCHAR(128),
         msgSenderSubject VARCHAR(128),
         msgText LONGTEXT
    )""".format(table) # change 'table' above if necessary
    # insert jokes here
    text = "This is a test message."
    # subject line for each email
    subject = "Jason's Joke of the Day"
    # return address 
    sender = '<a href="mailto:jmwoloso@asu.edu">jmwoloso@asu.edu</a>'
    #### END USER INPUT #############################################
    
    # let's see if the table already exists
    does_exist = check_please(login_info, database, table)
    # if not, we'll make it really quick
    if does_exist != 1:
        print("Database table DOES NOT exist!")
        set_table(login_info, TBLDEF)
        
    # alright, table exists, back to the messages
    message_dict = generate_messages(RECIPIENTS, 
                                     STARTTIME, 
                                     DAYCOUNT,
                                     text,
                                     subject,
                                     sender)
    # let's print one day's worth of emails really quick
    # to make sure the format is correct
    send_to_console(message_dict)
    
    # alrighty, messages are created, let's add them to
    # the database table
    save_to_db(message_dict, login_info, table)
    
    # if we get this far, everything went smoothly
    # and you're done
    print("Messages saved.")
    print("Have a great vacation!")

# the main loop is our friend (on Windows)
if __name__=="__main__":
    main()