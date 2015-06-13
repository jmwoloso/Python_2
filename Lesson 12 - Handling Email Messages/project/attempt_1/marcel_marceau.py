#!/usr/bin/python3
#
# A Program To Create An Email From Specified Arguments
#    marcel_marceau.py
#
# Created by: Jason Wolosonovich
#    03-29-2015
#
# Lesson 11 - Project Attempt 1
"""
Takes arguments and creates an email object using the arguments to setup
the email in the correct format
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def MIMEograph(email, message, attachments=None):
    """Create an email from arguments provided."""
    msg = MIMEMultipart()
    msg['To'] = email
    msg.attach(MIMEText(message, 
                        'plain')
               )
    if attachments:
        for item in attachments:
            msg.attach(MIMEMultipart(item))
    
    return msg.as_string()
    