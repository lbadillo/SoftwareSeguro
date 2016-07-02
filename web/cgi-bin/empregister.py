#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import constants
from connectdb import connectDB
from xml.sax.saxutils import escape
import crypt
cgitb.enable()

def manageError(cod, message):
  resp=message
  if cod == 1062:
    resp = "Este correo electronico ya fue registrado previamente"
  return resp

form = cgi.FieldStorage()

first_name=form.getvalue('first_name')
first_name = escape(first_name)
last_name=form.getvalue('last_name')
last_name = escape(last_name)
e_mail=form.getvalue('e_mail')
e_mail = escape(e_mail)
password=form.getvalue('password')
passcript= crypt.crypt(password,constants.getSalt())

db = connectDB()

cursor = db.cursor()

#sql = "insert into employee (name,lastName,email,password) values ('%s','%s','%s','%s') " % (first_name,last_name,e_mail,passcript)

try:
  cursor.execute("insert into employee (name,lastName,email,password) values (%s,%s,%s,%s) " , (first_name,last_name,e_mail,passcript))
  db.commit()
  respcod = 0
  respon="Felicidades!! Registro exitoso a  BankSafe!"
except MySQLdb.Error, e:
  db.rollback()
  respon= manageError(e.args[0], e.args[1])
  respcod=e.args[0]
  

constants.getHeaderHtml( "Nuevo Empleado")
print '<div class="well">'
print '<h3> %s</h3>' % (respon)
if respcod == 0:
   print "<a href = '../emplogin.html'> Volver a login</a>"
 
else:
   print "<a href = '../empregister.html'> Volver a registro</a>"
print '</div>'  
 
constants.getFooterHtml()  
print '</body>'
print '</html>'
 

db.close()
