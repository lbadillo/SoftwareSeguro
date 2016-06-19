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

  #clientId = self.request.GET.get('cid')
  clientId = int(form.getvalue('cid'))
  #state = self.request.GET.get('sta')
  state = int(form.getvalue('sta'))

  db = connectDB()

  cursor = db.cursor()

  sql = "UPDATE client SET state = '%d' WHERE idClient = '%d'" % (state, clientId)

  try:
    cursor.execute(sql)
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
