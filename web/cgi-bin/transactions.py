#!/usr/bin/python
import MySQLdb
import cgi, cgitb

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
  cursor.execute("SELECT * FROM transactions t JOIN client cf ON t.idClientFrom = cf.idClient JOIN client ct ON t.idClientTo = ct.idClient WHERE t.state = 0")
  # fetch all of the rows from the query
  data = cursor.fetchall()

  # print the rows
  print '<h2>Approve Transactions</h2><br/>'
  print "<table border='1'>"
  print '<th>Transaction Code</th>'
  print '<th>Name From</th>'
  print '<th>Last Name From</th>'
  print '<th>Name To</th>'
  print '<th>Last Name To</th>'
  print '<th>Amount</th>'
  print '<th>Approve</th>'
  for row in data:
    print '<tr>'
    print '<td>' + row[1] + '</td>'
    print '<td>' + row[8] + '</td>'
    print '<td>' + row[9] + '</td>'
    print '<td>' + row[17] + '</td>'
    print '<td>' + row[18] + '</td>'
    print '<td>' + str(row[3]) + '</td>'
    print "<td><a href='transactionupdate.py?tid=" + str(row[0]) + "&sta=1'>Appove</a>"
    print '<br/>'
    print "<a href='transactionupdate.py?tid=" + str(row[0]) + "&sta=2'>Reject</a></td>"
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
