#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import crypt
import os
import Cookie
from connectdb import connectDB
from constants import getSalt
cgitb.enable()



form = cgi.FieldStorage()


e_mail=form.getvalue('e_mail')
password=form.getvalue('password')
passcript= crypt.crypt(password,getSalt())
respon = "no"
idClient = 0


db = connectDB()

cursor = db.cursor()




sql = "select idClient from client where email = '%s' and password = '%s' and state = 1"  % (e_mail,passcript)

try:
  cursor.execute(sql)
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
  c=Cookie.SimpleCookie()
  c['idusuario']=idClient
  print c 
  print "Location: clientoptions.py\r\n"
else:
  print "Content-type: text/html\r\n\r\n"
  print "<!DOCTYPE html>"
  print '<html>'
  print '<head>'
  print '<title>Error</title>'
  print '</head>'
  print '<body>'
  print "<h2>%s</h2><br>" %(respon)
  print "<a href = '../loginclient.html'> Login Cliente </a>"
  print '</body>'
  print '</html>'









