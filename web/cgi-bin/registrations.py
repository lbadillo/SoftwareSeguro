#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import constants

cgitb.enable()

respon = "Usuario No Registrado"
idClient = constants.getClientCookie()

constants.getHeaderHtml( "Opciones Cliente")
print '<div class="well">'
if idClient!="0":

  #db = connectDB()
  db = MySQLdb.connect("localhost","root","samurai","banksafe")
  cursor = db.cursor()
  #if conn.is_connected():
  #    print('Connected to MySQL database')
  cursor.execute("SELECT * FROM client WHERE state = 0")
  # fetch all of the rows from the query
  data = cursor.fetchall()

  # print the rows
  print '<h2>Approve Registrations</h2><br/>'
  print "<table border='1'>"
  print '<th>Email</th>'
  print '<th>Name</th>'
  print '<th>Last Name</th>'
  print '<th>Amount</th>'
  print '<th>Approve</th>'
  for row in data:
      print '<tr>'
      print '<td>' + row[3] + '</td>'
      print '<td>' + row[1] + '</td>'
      print '<td>' + row[2] + '</td>'
      print '<td>' + str(row[5]) + '</td>'
      print "<td><a href='clientupdate.py?cid=" + str(row[0]) + "&sta=1'>Appove</a>"
      print '<br/>'
      print "<a href='clientupdate.py?cid=" + str(row[0]) + "&sta=2'>Reject</a></td>"
      print '</tr>'

  print '</table>'
  print '<br/>'
  print "<a href='empmenu.py'>Go Back</a>"
  print '</body>'
  print '</html>'

  db.close()
else:
  print "<h3>%s</h3><br>" %(respon)
  print "<a href = '../emplogin.html'> Login Empleado </a>"
print '</div>'  
constants.getFooterHtml()  
print '</body>'
print '</html>'
