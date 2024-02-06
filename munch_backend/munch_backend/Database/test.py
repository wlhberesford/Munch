'''
Test file made to figure out how a data base will be made

Created: 
- Liam Beresford  -  2/6/2024

'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")