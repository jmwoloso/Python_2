#!/usr/bin/python
import time, sys
from datetime import datetime, timedelta, date
from email.utils import make_msgid
from email.message import Message
import matplotlib.pyplot as plt
import numpy as np


RECIPIENTS = [('Pat Barton', 'learn@oreilly.com'),
              ('Jason Wolosonovich', 'jmwoloso@asu.edu')]

STARTTIME = datetime.date(datetime.strptime('07/04/2015', '%m/%d/%Y'))

DAYCOUNT = [1,10,50,100,500]
timing_list = []
subject = "Jason's Joke of the Day"
# person sending the email
sender = '<a href="mailto:jmwoloso@asu.edu">jmwoloso@asu.edu</a>'        
# message content
text = """A pirate walks into a bar with a ship's steering wheel hanging from his
crotch:

Bartender: "What the hell is that?"
Pirate: "I don't know but it's driving me nuts!" """ 

def generate_messages(RECIPIENTS=None, STARTTIME=None, DAYS=None, text=None, subject=None, sender=None):
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
    for i in range(0, DAYS):
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
        
        message_dict[STARTTIME.strftime('%m/%d/%Y')] = message_list
        # increment STARTTIME by one day and do it all over again
        STARTTIME += timedelta(days=1)
                    
    return message_dict

def plot_results(message_dict=None, timing_list=None, DAYCOUNT=None):
    msgs_per_second = []
    print(timing_list)
    print("\n#### TIMING RESULTS ####")
    for i in range(0, len(timing_list)):
        print("{0} --> {1} seconds".format(timing_list[i][0], timing_list[i][1]))
        msgs_per_second.append(DAYCOUNT[i] / (timing_list[i][1] + 0.00000000001))
    print("\n\n#### MESSAGE GENERATION TIMES ####")
    
    for i, DAYS in enumerate(DAYCOUNT):
        print("Messages per Second: {0}".format(msgs_per_second[i]))
        print("Number of Messages: {0}".format(DAYS))
        print("Time to Generate: {0} seconds\n".format(timing_list[i][1]))
    print(len(timing_list))
    print(len(DAYCOUNT))
    times = []
    for i in range(0, len(timing_list)):
        times.append(timing_list[i][1])
    
    print(msgs_per_second)
    plt.figure(1)
    plt.scatter(DAYCOUNT, times, c='g', marker='o')
    
    plt.ylabel('Time (s)')
    plt.xlabel('Messages Generated')
    plt.title('Time (seconds) vs. Messages Generated')
    plt.grid()
    
    plt.figure(2)
    plt.plot(np.log10(msgs_per_second), 'ro')
    plt.ylabel('Log10 (Messages Per Second)')
    plt.xlabel('Iterations')
    plt.ylim(ymin=-1, ymax=15)
    plt.xlim(xmin=-1, xmax=6)
    plt.title('Messages per Second at Each DAYCOUNT Iteration')
    
    plt.grid()
    plt.show()
def main():
    #message_dict, timing_list = generate_messages(RECIPIENTS, STARTTIME, DAYCOUNT, text, subject, sender)
    #plot_results(message_dict, timing_list, DAYCOUNT)
    
    for DAYS in DAYCOUNT:
        start = time.time()
        message_dict = generate_messages(RECIPIENTS, STARTTIME, DAYS, text, subject, sender)
        end = time.time()
        timing_list.append(("DAYCOUNT={0}".format(DAYS), end - start))
    
    plot_results(message_dict, timing_list, DAYCOUNT)
if __name__=="__main__":
    main()