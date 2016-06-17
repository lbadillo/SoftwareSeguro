#!/usr/bin/python
import MySQLdb
import cgi, cgitb
from constants import getClientCookie
from connectdb import connectDB

cgitb.enable()

idClient = getClientCookie()
respon ="Usuario No Registrado"
form = cgi.FieldStorage()
codeTran = form.getvalue('codeTran')
amount= float(form.getvalue('amount'))
typeTran = "2"
destination = form.getvalue('destination')
balance = float(form.getvalue('balance'))
sql2="ok"
state="0"
amount2 = "-101"
if idClient != "0":
  respon = "No se pudo realizar la Transaccion"
  print "Content-type: text/html\r\n\r\n"
  print "<!DOCTYPE html>"  
  print '<html>'
  print '<head>'
  print '<title>Nueva Transaccion</title>'
  print '</head>'
  print '<body>'
  db = connectDB()
  cursor = db.cursor()
  if amount<10000:
    state="1"
  
  total= balance-amount
  if total<0:
    respon = "Fondos Insuficientes para esta transaccion"
  else:
    sql3 ="select amount from client where state = 1 and idclient = %s"%(destination)
    try:
      cursor.execute(sql3)
      row = cursor.fetchone()
      if row is not None:
	amount2 = row[0]
	total2= float(amount2)+amount
	sql4="update client set amount= %s  where idclient=%s"%(total2,destination)
      else:  
	respon = "Cliente destino no existe"
	  
    except:
      amount2="-101"
      respon = "Cliente destino no existe" 
      
    if amount2 != "-101":
      sql = "insert into transactions (codetransaction,typetransaction,amount,idclientfrom,idclientto,state) values ('%s',%s,%s,%s,%s,%s) "  % (codeTran,typeTran,amount,idClient,destination,state)
      if state=="1":
	sql2="update client set amount= %s, consecutive = consecutive+1 where idclient=%s"%(total,idClient)
	respon = "Transacccion [%s] exitosa"%codeTran		
      else:
	sql2="update client set consecutive = consecutive+1 where idclient=%s"%(idClient)
	sql4="select 1 from dual"
	respon = "Transaccion [%s] exitosa: Pendiente por aprobacion"%codeTran      
      try:	  
	cursor.execute(sql)
	cursor.execute(sql2)
	cursor.execute(sql4)
	db.commit()      
      except MySQLdb.Error, e:
	db.rollback()
	respon = "No se pudo realizar la Transaccion:%s"%e.args[1]
	  
  print '<h2> %s</h2>' % (respon)     
  print "<a href = 'newtrans.py'> Volver a transacciones </a>"
  print '</body>'
  print '</html>'

db.close()


