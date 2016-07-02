#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import constants 
from connectdb import connectDB

cgitb.enable()

idClient = constants.getClientCookie()
respon ="Usuario No Registrado"
form = cgi.FieldStorage()
codeTran = form.getvalue('codeTran')
amount= float(form.getvalue('amount'))
typeTran = "2"
destination = form.getvalue('destination')

sql2="ok"
state="0"
amount2 = "-101"
respon = "No se pudo realizar la Transaccion"
constants.getHeaderHtml( "Registrar Transaccion")

if idClient != "0":
    db = connectDB()
    cursor = db.cursor()
    if amount<10000:
        state="1"
    sqlb="select pin, amount from client where idClient=%s"%idClient
    cursor.execute(sqlb)
    try:
        rowb= cursor.fetchone()
        if rowb is not None:
            pin1=rowb[0]
            balance = rowb[1]
            total= float(balance)-amount

        else:
            pin1="-1"
            total=-1
    except:
        respon = "El cliente no esta registrado"
       
    if total<0:
        respon = "Fondos Insuficientes para esta transaccion"
    else:
        sql3 ="select amount, idClient, pin from client where state = 1 and email = '%s'"%(destination)
    
        try:
            cursor.execute(sql3)
            row = cursor.fetchone()
            if row is not None:
                amount2 = row[0]
                idClient2=row[1]
                total2= float(amount2)+amount
                pin2=row[2]
                if pin1 != "-1":
                    if constants.testToken(pin1,pin2, codeTran, amount):
                        sql4="update client set amount= %s  where idClient='%s'"%(total2,idClient2)
                        sql = "insert into transactions (codetransaction,typetransaction,amount,idclientfrom,idclientto,state) values ('%s',%s,%s,%s,%s,%s) "  % (codeTran,typeTran,amount,idClient,idClient2,state)
                    else:
                        amount2="-101"
                        respon="Codigo Transaccion no Valido"
            else:  
                respon = "Cliente destino no existe"
          
        except:
            amount2="-101"
            respon = "Cliente destino no existe" 
        if amount2 != "-101":
            if state=="1":
                sql2="update client set amount= %s, consecutive = consecutive+1 where idclient=%s"%(total,idClient)
                respon = "Transacccion [%s] exitosa"%codeTran           
            else:
                sql2="update client set consecutive = consecutive+1 where idclient=%s"%(idClient)
                sql4="select 1 from dual"
                respon = "Transaccion [%s] exitosa: Pendiente por aprobacion"%codeTran      
            try:
                if str(idClient2) != str(idClient):
                    
                    cursor.execute(sql)
                    cursor.execute(sql2)
                    cursor.execute(sql4)
                    db.commit()
                else:  
                    respon = "El usuario origen y destino son los mismos"
            except MySQLdb.Error, e:
                db.rollback()
                respon = "No se pudo realizar la Transaccion:%s"%e.args[1]  
      
print '<div class="well">' 
print '<h4> %s</h4>' % (respon) 
print '</div>'
print "<a href = 'newtrans.py'> Volver a transacciones </a>"
constants.getFooterHtml()   
print '</body>'
print '</html>'


try:
  db.close()
except:
  print ''


