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
idEmployee = 0


db = connectDB()

cursor = db.cursor()

sql = "select idEmployee from employee where email = '%s' and password = '%s'"  % (e_mail,passcript)

try:
  cursor.execute(sql)
  row = cursor.fetchone()
  if row is not None:
    idEmployee = row[0]
    respon="ok"
  else:
    respon="Usuario Invalido"
    
except MySQLdb.Error, e:
  respon="Usuario Invalido"

db.close()


if idClient>0:
  c=Cookie.SimpleCookie()
  c['idusuario']=idEmployee
  print c 
  print "Location: empmenu.py\r\n"
else:
  constants.getHeaderHtml( "Control Usuarios")
  print "<h4>%s</h4><br>" %(respon)
  constants.getFooterHtml() 
  print "<a href = '../emplogin.html'> Login Empleado </a>"
  print '</body>'
  print '</html>'
