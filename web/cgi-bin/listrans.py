#!/usr/bin/python
import MySQLdb
import cgi, cgitb
from constants import getClientCookie
from connectdb import connectDB

cgitb.enable()

idClient = getClientCookie()
respon ="Usuario No Registrado"

    
print "Content-type: text/html\r\n\r\n"
print "<!DOCTYPE html>"  
print '<html>'
print '<head>'
print '<title>Listado Transacciones</title>'
print '</head>'
print '<body>'
if idClient != "0":
  db = connectDB()
  cursor = db.cursor()
  
  sql = "select Code, Type, Amount, Origin, Destination, State from vw_transactionlist where idclient = '%s' "  % (idClient)
  try:
    cursor.execute(sql)
    results = cursor.fetchall()
    num_fileds = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    print '<table>'
    print '<tr>'
    for names in field_names:
       print "<th>%s</th>" % (names)
    print '</tr>'  
   
    for row in results:
      print '<tr>'
      for lrow in row:
	if lrow is not None:
	  print "<td>%s</td>" % (lrow)
	else:
	   print "<td>--</td>"
      print '</tr>'
    print '</table>' 
    print "<br>"
  
  except MySQLdb.Error, e:
    print 'Error en la generacion de la consulta'
  print "<a href = 'clientoptions.py'> Volver a opciones </a>"      
else:    
  print '<h2> %s</h2><br>' % (respon) 
  print "<a href = '../loginclient.html'> Volver a login</a>"
print '</body>'
print '</html>'

db.close()


