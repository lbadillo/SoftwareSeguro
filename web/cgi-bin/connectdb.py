#!/usr/bin/python
import MySQLdb
import cgi, cgitb
cgitb.enable()

def connectDB():
  db = MySQLdb.connect("localhost","root","samurai","banksafe")
  return db
  