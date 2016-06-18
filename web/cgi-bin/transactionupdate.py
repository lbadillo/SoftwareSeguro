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

  form = cgi.FieldStorage()

  transactionId = int(form.getvalue('tid'))
  state = int(form.getvalue('sta'))

  db = MySQLdb.connect("localhost","root","samurai","banksafe")

  cursor = db.cursor()

  sql = "UPDATE transactions SET state = '%d' WHERE idTransaction = '%d'" % (state, transactionId)
  sql2 = "SELECT @idClientFrom:=idClientFrom, @idClientTo:=idClientTo, @flAmount:=amount,@intTypeTransaction:=typeTransaction FROM transactions WHERE idTransaction = '%d';" % (transactionId)
  sql3 = "UPDATE client SET amount = amount-@flAmount WHERE idClient = @idClientFrom;"
  sql4 = "UPDATE client SET amount = amount+@flAmount WHERE idClient = @idClientTo;"

  try:
    cursor.execute(sql)
    if state is 1:
      cursor.execute(sql2)
      cursor.execute(sql3)
      cursor.execute(sql4)
    db.commit()
    respcod = 0
    respon="Transaction updated!!"
  except MySQLdb.Error, e:
    db.rollback()
    respon= manageError(e.args[0], e.args[1])
    respcod=e.args[0]

  print '<h2> %s</h2>' % (respon)
  print "<a href='registrations.py'>Back to Approve registrations</a>"
  print '<br/>'
  print "<a href='transactions.py'>Back to Approve transactions</a>"

  db.close()
else:
  print "<h3>%s</h3><br>" %(respon)
  print "<a href = '../emplogin.html'> Login Empleado </a>"
print '</div>'  
constants.getFooterHtml()  
print '</body>'
print '</html>'
