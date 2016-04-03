#!/usr/bin/python
#
# For using mysql in python , need to install mysql-python connector.For installing that run below commands for linux systems
# 	for debian based distro : sudo apt-get install python-mysqldb
# 	for rpm based distro : yum install mysql-python
#
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="username",         # your username
                     passwd="password",  # your password
                     db="databasename")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
