#!/usr/bin/python
import cgi, cgitb
import constants 
cgitb.enable()


respon = "Usuario No Registrado"
idClient = constants.getClientCookie()

constants.getHeaderHtml( "Opciones Cliente")
print '<div class="well">'
if idClient!="0":
  
  print '<div class="list-group margin-b-3">'
  print '<a href="#" class="active list-group-item"><h3>Acciones</h3></a>'
  print "<a href = 'clientdata.py' class='list-group-item'><h4> Perfil </h4></a>"
  print "<a href = 'listrans.py' class='list-group-item'><h4> Ver listado de Transacciones</h4></a>"
  print "<a href = 'newtrans.py' class='list-group-item'><h4> Hacer una Transaccion</h4></a>"
  print "<a href = '../uploadfile.html' class='list-group-item'><h4> Generar Transacciones Batch</h4></a>"
  print '</div>'
  
else:
  print "<h3>%s</h3><br>" %(respon)
  print "<a href = '../loginclient.html'> Login Cliente </a>"
print '</div>'  
constants.getFooterHtml()  
print '</body>'
print '</html>'









