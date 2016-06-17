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
print '<title>Nueva Transaccion</title>'
print '</head>'
print '<body>'
if idClient != "0":
  db = connectDB()
  cursor = db.cursor()
  
  sql = "select consecutive, maxcode, amount from client where idclient = '%s' "  % (idClient)
  try:
    cursor.execute(sql)
    row = cursor.fetchone()
    
    if row is not None:
      cons = int(row[0])
      maxval = int(row[1])
      balance = row[2]
      if cons>=maxval:
	print '<h2>No hay codigos de transacciones disponibles</h2><br>' 
      else:
	cons = cons+1
        codeTran=idClient+"-"+str(cons)
        
        print '<form action="/cgi-bin/savetran.py" method="post">'
        print '<input type="hidden" name="codeTran" value="%s">' %codeTran
        print '<input type="hidden" name="balance" value="%s">' %balance
        
        print '<table>'
        
        print '<tr>'
        print '<td>'
        print 'Codigo Transaccion'
        print '</td>'
        print '<td>'
        print '%s'%codeTran
        print '</td>'
	print '</tr>'
	
	
	print '<tr>'
        print '<td>'
        print 'Cuenta Destino'
        print '</td>'
        print '<td>'
        print '<input type="number" name="destination" required/>'
        print '</td>'
	print '</tr>'
	
	print '<tr>'
        print '<td>'
        print 'Valor'
        print '</td>'
        print '<td>'
        print '<input type="number" name="amount" min="1" required/>'
        print '</td>'
	print '</tr>'
	
	print '<tr>'
        print '<td>'
        print '<input type="submit" value="submit" />'
        print '</td>'
        
	print '</tr>'
	
	print '</table>' 
	
	print '</form>'
	print "<br>"
	print "<a href = 'clientoptions.py'> Volver a opciones </a>"
   
   
  except MySQLdb.Error, e:
    respon2 = 'Error en la generacion de la consulta'
else:    
  print '<h2> %s</h2><br>' % (respon) 
  print "<a href = '../loginclient.html'> Volver a login</a>"
print '</body>'
print '</html>'

db.close()


