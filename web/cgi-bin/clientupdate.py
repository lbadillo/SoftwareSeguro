#!/usr/bin/python
import MySQLdb
import cgi, cgitb
cgitb.enable()

respon = "Usuario No Registrado"
idClient = constants.getClientCookie()

constants.getHeaderHtml( "Opciones Cliente")
print '<div class="well">'
if idClient!="0":

  form = cgi.FieldStorage()

  #clientId = self.request.GET.get('cid')
  clientId = int(form.getvalue('cid'))
  #state = self.request.GET.get('sta')
  state = int(form.getvalue('sta'))

  db = MySQLdb.connect("localhost","root","samurai","banksafe")

  cursor = db.cursor()

  sql = "UPDATE client SET state = '%d' WHERE idClient = '%d'" % (state, clientId)

  try:
    cursor.execute(sql)
    db.commit()
    respcod = 0
    respon="Reigster updated!!"
  except MySQLdb.Error, e:
    db.rollback()
    respon= manageError(e.args[0], e.args[1])
    respcod=e.args[0]

  import bankmailer
  if state is 1:
    bankmailer.sendmail(clientId)

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
