#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import crypt
from connectdb import connectDB
from constants import getSalt
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
passcript= crypt.crypt(password,getSalt())
amount=form.getvalue('amount')

db = connectDB()

cursor = db.cursor()




sql = "insert into client (name,lastName,email,password, amount,state) values ('%s','%s','%s','%s','%s','%d') " % (first_name,last_name,e_mail,passcript,amount,0)

try:
  cursor.execute(sql)
  db.commit()
  respcod = 0
  respon="Felicidades!!!!  Despues de efectuar el proceso de verificacion sera enviado un correo de bienvenida a nuestro banco"
except MySQLdb.Error, e:
  db.rollback()
  respon= manageError(e.args[0], e.args[1])
  respcod=e.args[0]



  
print "Content-type: text/html\r\n\r\n";
print '<html>'
print '<head>'
print '<title>Registro Cliente</title>'
print '</head>'
print '<body>'
print '<h2> %s</h2>' % (respon)
if respcod == 0:
   print "<a href = '../loginclient.html'> Volver a login</a>"
 
else:
   print "<a href = '../register.html'> Volver a registro</a>"
  
 
  
print '</body>'
print '</html>'

db.close()