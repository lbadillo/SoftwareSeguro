#!/usr/bin/python
import MySQLdb
import cgi, cgitb
cgitb.enable()

def connectDB():
  db = MySQLdb.connect("localhost","root","cristi79","banksafe")
  return db
  