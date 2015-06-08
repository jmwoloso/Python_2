#!/usr/bin/python3
# Container for DB Credentials
#    database.py
#
# Created by: Jason Wolosonovich
#    04-25-2015
#
# Lesson 13- Project Attempt 1
"""
Simply holds login credentials and info used to access a MySQL DB.
This is the specific format required for the _mysql module in python
since mysql can't be installed with Canopy.
"""

USERNAME = "jwoloson"
PASSWORD = "Jmw4804143507"

login_info = {
              'host': "cold.oreillyschool.com",
              'user': USERNAME,
              'passwd': PASSWORD,
              'db': USERNAME,
              'port': 3306
              }
