#!/usr/bin/python3
#
# A Program To Query An Email Database And Return Formatted Results
#    settings.py
#
# Created by: Jason Wolosonovich
#    04-25-2015
#
# Lesson 13 - Project Attempt 1
"""
Holds the python names used to generate and send emails via
gone_fishin.py
"""
from datetime import datetime


# Recipients of the jotd emails
# form should be a list of tuples of the form ('First Last', 'email@email.com')
RECIPIENTS = [('Pat Barton', 'learnb@oreillyschool.com'),
              ('Jason W.', 'jmwoloso@asu.edu')]

# Date to start sending generated jotd emails
STARTTIME = datetime.date(datetime.strptime('07/04/2015', '%m/%d/%Y'))

# Number of emails to generate each day
DAYCOUNT = 500