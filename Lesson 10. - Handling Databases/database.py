#!/usr/bin/python3
# Container for DB Credentials
#    database.py
#
# Created by: Jason Wolosonovich
#    03-19-2015
#
# Lesson 10 - Exercise 2
"""
Simply holds login credentials and info used to access a MySQL DB.
"""

USERNAME = "jwoloson"
PASSWORD = "Jmw4804143507"

login_info = {
              'host': "sql.oreillyschool.com",
              'user': USERNAME,
              'password': PASSWORD,
              'database': USERNAME,
              'port': 3306
              }
