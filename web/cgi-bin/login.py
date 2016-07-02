#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import crypt
import os
import Cookie
from connectdb import connectDB
import constants
cgitb.enable()



form = cgi.FieldStorage()


e_mail=form.getvalue('e_mail')
password=form.getvalue('password')
passcript= crypt.crypt(password,constants.getSalt())
respon = "no"
idClient = 0


db = connectDB()

cursor = db.cursor()




#sql = "select idClient from client where email = '%s' and password = '%s' and state = 1"  % (e_mail,passcript)

try:
  cursor.execute("select idClient from client where email = %s and password = %s and state = 1"  , (e_mail,passcript))
  row = cursor.fetchone()
  if row is not None:
    idClient = row[0]
    respon="ok"
  else:
    respon="Usuario Invalido"
    
except MySQLdb.Error, e:
  respon="Usuario Invalido"

db.close()


if idClient>0:
  constants.setClientCookie(idClient)
  print "Location: clientoptions.py\r\n"
else:
  constants.getHeaderHtml( "Control Usuarios")
  print "<h4>%s</h4><br>" %(respon)
  constants.getFooterHtml() 
  print "<a href = '../loginclient.html'> Login Cliente </a>"
  print '</body>'
  print '</html>'









