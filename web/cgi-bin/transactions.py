#!/usr/bin/python
import MySQLdb
import cgi, cgitb
from connectdb import connectDB
import constants

cgitb.enable()

respon = "Usuario No Registrado"
idClient = constants.getEmployeeCookie()

constants.getHeaderHtml( "Listado Transacciones Pendientes")

if idClient!="0":
  
  db = connectDB()
  cursor = db.cursor()
  cursor.execute("SELECT t.idtransaction, t.codeTransaction,cf.name,cf.lastname, ct.name,ct.lastname, t.amount FROM transactions t JOIN client cf ON t.idClientFrom = cf.idClient JOIN client ct ON t.idClientTo = ct.idClient WHERE t.state = 0")
  # fetch all of the rows from the query
  data = cursor.fetchall()

  # print the rows

  print "<table class='table table-hover'>"
  print '<th>Codigo</th>'
  print '<th>Nombre Origen</th>'
  print '<th>Apellido Origen</th>'
  print '<th>Nombre Destino</th>'
  print '<th>Apellido Detino</th>'
  print '<th>Valor</th>'
  print '<th>Opcion</th>'
  for row in data:
    print '<tr>'
    print '<td>' + row[1] + '</td>'
    print '<td>' + row[2] + '</td>'
    print '<td>' + row[3] + '</td>'
    print '<td>' + row[4] + '</td>'
    print '<td>' + row[5] + '</td>'
    print '<td>' + str(row[6]) + '</td>'
    print "<td><a href='transactionupdate.py?tid=" + str(row[0]) + "&sta=1'>Appove</a>"
    print '<br/>'
    print "<a href='transactionupdate.py?tid=" + str(row[0]) + "&sta=2'>Reject</a></td>"
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
