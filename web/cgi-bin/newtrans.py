#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import  constants 
from connectdb import connectDB

cgitb.enable()

idClient = constants.getClientCookie()
respon ="Usuario No Registrado"

    
constants.getHeaderHtml( "Nueva Transaccion")
if idClient != "0":
  db = connectDB()
  cursor = db.cursor()
  
  sql = "select consecutive, maxcode from client where idclient = '%s' "  % (idClient)
  try:
    cursor.execute(sql)
    row = cursor.fetchone()
    
    if row is not None:
      cons = int(row[0])
      maxval = int(row[1])
      
      if cons>=maxval:
	print '<h2>No hay codigos de transacciones disponibles</h2><br>' 
	print "<a href = 'clientoptions.py'> Volver a opciones </a>"  
      else:
	cons = cons+1
        codeTran=idClient+"-"+str(cons)
        
        print '<div class="well">'
        print '<form action="/cgi-bin/savetran.py" method="post">'
       
       
        print '<div class="form-group">'
        print '  <label>Codigo Transaccion</label>' 
        print '  <input type="text" name="codeTran"  class="form-control" required/>' 
        print '</div>'
        
        print '<div class="form-group">'
        print '  <label>Usuario Destino</label>' 
        print '  <input type="text" name="destination" required class="form-control" />'
        print '</div>'
        
        print '<div class="form-group">'
        print '  <label>Valor</label>' 
        print '<input type="number" name="amount" min="1" required class="form-control"/>'
        print '</div>'
        print '<input type="submit" value="Enviar" class="btn btn-default"/>'
        print '</form>'
        print '</div>' 
        print "<a href = 'clientoptions.py'> Volver a opciones </a>"  
  except MySQLdb.Error, e:
    respon2 = 'Error en la generacion de la consulta'
  
else:    
  print '<h2> %s</h2><br>' % (respon) 
  print "<a href = '../loginclient.html'> Volver a login</a>"
 
constants.getFooterHtml()    
print '</body>'
print '</html>'

try:
  db.close()
except:
  print ''


