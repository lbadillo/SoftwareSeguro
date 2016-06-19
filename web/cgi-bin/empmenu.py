#!/usr/bin/python
import cgi, cgitb
import constants
cgitb.enable()

respon = "Usuario No Registrado"
idClient = constants.getEmployeeCookie()

constants.getHeaderHtml( "Opciones Empleado")
print '<div class="well">'
if idClient!="0":
  
  print '<div class="list-group margin-b-3">'
  print '<a href="#" class="active list-group-item"><h3>Acciones</h3></a>'
  print "<a href='registrations.py' class='list-group-item'>Aprobar Nuevos Clientes</a>"
  print "<a href='transactions.py' class='list-group-item'>Aprobar Transacciones</a>"
  print '</div>'
  
else:
  print "<h3>%s</h3><br>" %(respon)
  print "<a href = '../emplogin.html'> Login Empleado </a>"
print '</div>'  
constants.getFooterHtml()  
print '</body>'
print '</html>'


