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
  cursor.execute("SELECT idClient, name,lastname,  email, amount FROM client WHERE state = 0")
  # fetch all of the rows from the query
  data = cursor.fetchall()

  # print the rows

  print "<table class='table table-hover'>"
  print '<th>Correo</th>'
  print '<th>Nombre</th>'
  print '<th>Apellido</th>'
  print '<th>Saldo Inicial</th>'
  print '<th>Opciones</th>'
  for row in data:
      print '<tr>'
      print '<td>' + row[3] + '</td>'
      print '<td>' + row[1] + '</td>'
      print '<td>' + row[2] + '</td>'
      print '<td>' + str(row[4]) + '</td>'
      print "<td><form action='/cgi-bin/clientupdate.py' method='post'>"
      print '<input type= "radio" name="valor" value="1-'+str(row[0])+'"> Aceptar<br>'
      print '<input type= "radio" name="valor" value="2-'+str(row[0])+'"> Rechazar<br>'
      print '<input type="submit" value="Enviar" class="btn btn-default"/> '
      print "</form> </td>"
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
