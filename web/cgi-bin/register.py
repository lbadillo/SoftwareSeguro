#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import crypt
from connectdb import connectDB
import constants
cgitb.enable()

def manageError(cod, message):
  resp=message
  if cod == 1062:
    resp = "Este correo electronico ya fue registrado previamente"
  return resp

form = cgi.FieldStorage()

first_name=form.getvalue('first_name')
last_name=form.getvalue('last_name')
e_mail=form.getvalue('e_mail')
password=form.getvalue('password')
passcript= crypt.crypt(password,constants.getSalt())
amount=form.getvalue('amount')
pin = constants.getPinClient(e_mail)

db = connectDB()

cursor = db.cursor()




sql = "insert into client (name,lastName,email,password,pin, amount,state) values ('%s','%s','%s','%s','%s','%s','%d') " % (first_name,last_name,e_mail,passcript,pin,amount,0)

try:
  cursor.execute(sql)
  db.commit()
  respcod = 0
  respon="Felicidades!!!!  Despues de efectuar el proceso de verificacion sera enviado un correo de bienvenida a nuestro banco"
except MySQLdb.Error, e:
  db.rollback()
  respon= manageError(e.args[0], e.args[1])
  respcod=e.args[0]
  
constants.getHeaderHtml( "Nuevo Cliente")
print '<div class="well">'
print '<h3> %s</h3>' % (respon)
if respcod == 0:
   print "<a href = '../loginclient.html'> Ir a login</a>"
 
else:
   print "<a href = '../register.html'> Volver a registro</a>"
print '</div>'  
 
constants.getFooterHtml()  
print '</body>'
print '</html>'

db.close()