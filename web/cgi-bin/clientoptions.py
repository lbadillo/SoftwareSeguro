#!/usr/bin/python
import cgi, cgitb
from constants import getClientCookie
cgitb.enable()


respon = "Usuario No Registrado"
idClient = getClientCookie()

print "Content-type: text/html\r\n\r\n"
print "<!DOCTYPE html>"  
print '<html>'
print '<head>'
print '<title>Listado Transacciones</title>'
print '</head>'
print '<body>'
if idClient!="0":
  print "<a href = 'listrans.py'> Ver listado de Transacciones</a><br>"
  print "<a href = 'newtrans.py'> Hacer una Transaccion</a>"
else:
  print "<h2>%s</h2><br>" %(respon)
  print "<a href = '../loginclient.html'> Login Cliente </a>"
print '</body>'
print '</html>'









