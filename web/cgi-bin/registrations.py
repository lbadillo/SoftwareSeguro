#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import constants
from connectdb import connectDB
cgitb.enable()

respon = "Usuario No Registrado"
idClient = constants.getEmployeeCookie()

constants.getHeaderHtml( "Clientes Pendientes")

if idClient!="0":

  db = connectDB()
  cursor = db.cursor()
  cursor.execute("SELECT * FROM client WHERE state = 0")
  # fetch all of the rows from the query
  data = cursor.fetchall()

  # print the rows
  print "<table class='table table-hover'>"
  print '<th>Correo</th>'
  print '<th>Nombre</th>'
  print '<th>Apellido</th>'
  print '<th>Saldo Inicial</th>'
  print '<th>Opcion</th>'
  for row in data:
      print '<tr>'
      print '<td>' + row[3] + '</td>'
      print '<td>' + row[1] + '</td>'
      print '<td>' + row[2] + '</td>'
      print '<td>' + str(row[5]) + '</td>'
      print "<td><a href='clientupdate.py?cid=" + str(row[0]) + "&sta=1'>Aprobar</a>"
      print '<br/>'
      print "<a href='clientupdate.py?cid=" + str(row[0]) + "&sta=2'>Rechazar</a></td>"
      print '</tr>'

  print '</table>'
  print '<br/>'
  print "<a href='empmenu.py'>Volver a Opciones</a>"
  print '</body>'
  print '</html>'

  db.close()
else:
  print "<h3>%s</h3><br>" %(respon)
  print "<a href = '../emplogin.html'> Login Empleado </a>"

constants.getFooterHtml()  
print '</body>'
print '</html>'