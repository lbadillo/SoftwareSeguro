#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import constants
from connectdb import connectDB
import bankmailer
cgitb.enable()

respon = "Usuario No Registrado"
idClient = constants.getEmployeeCookie()

constants.getHeaderHtml( "Aprobar Clientes")
print '<div class="well">'
if idClient!="0":

  form = cgi.FieldStorage()

  if form.getvalue('valor'):
     valor = form.getvalue('valor')
     clientId= valor[2:]
     state = valor[:1]
  else:
    clientId= '0'
    state = '0'

  db = connectDB()

  cursor = db.cursor()

  #sql = "UPDATE client SET state = %s WHERE idClient = %s" , (state, clientId)

  try:
    cursor.execute("UPDATE client SET state = %s WHERE idClient = %s" , (state, clientId))
    db.commit()
    respcod = 0
    respon="Registro Actualizado"
  except MySQLdb.Error, e:
    db.rollback()
    respon= manageError(e.args[0], e.args[1])
    respcod=e.args[0]

 
  if state is 1:
    bankmailer.sendmail(clientId)

  print '<h2> %s</h2>' % (respon)
  print "<a href='registrations.py'>Volver Clientes Pendientes</a>"
 

  db.close()
else:
  print "<h3>%s</h3><br>" %(respon)
  print "<a href = '../emplogin.html'> Login Empleado </a>"
print '</div>'  
constants.getFooterHtml()  
print '</body>'
print '</html>'
