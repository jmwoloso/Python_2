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

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

def MIMEograph(email, message, attachments=None):
    """Create an email from arguments provided."""
    msg = MIMEMultipart()
    msg['To'] = email
    msg.attach(MIMEText(message, 
                        'plain')
               )
    if attachments:
        for item in attachments:
            print(item)
            # figure out ctype and encoding of attachment
            ctype, encoding = mimetypes.guess_type(item)
            
            # if ctype/encoding can't be determined so use generic type
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/',
                                             1)
            
            # if file type is text
            if maintype == 'text':
                with open(item) as f:
                    a = MIMEText(f.read(), 
                                 _subtype=subtype)
            
            # if filetype is an image
            elif maintype == 'image':
                with open(item, 'rb') as f:
                    a = MIMEImage(f.read(), 
                                  _subtype=subtype)
                                
            # if filetype is audio
            elif maintype == 'audio':
                with open(item, 'rb') as f:
                    a = MIMEAudio(f.read(), 
                                  _subtype=subtype)
            
            # if none of the above use base message class
            else:
                with open(item, 'rb') as f:
                    a = MIMEBase(maintype, 
                                 subtype)
                    a.set_payload(f.read())
                    # use base64 encoding
                    encoders.encode_base64(a)
            # set filename header
            a.add_header('Content-Disposition', 
                         'attachment', 
                         filename=os.path.basename(item))
            # add attachment to message object after processing
            msg.attach(a)
            
    
    return msg.as_string()
    