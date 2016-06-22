#!/usr/bin/python
import smtplib
import MySQLdb
from connectdb import connectDB

def sendmail(clientId):
	fromaddr = 'softwaresegurobanco@gmail.com'
	
	db = connectDB()
	cursor = db.cursor()
	sql = "SELECT pin,consecutive, maxcode, email  FROM client WHERE idClient = '%d'" % (clientId)
	cursor.execute(sql)
	# fetch all of the rows from the query
	data = cursor.fetchall()

	msg = 'Subject:Bienvenida BankSafe\n\nSu registro ha sido aprobado, bienvenido a BankSafe!!\n\n Para generar transacciones debe utilizar nuestra aplicacion de generacion de tokens utilizando los siguiente datos:\n\n'
	for row in data:
		toaddrs = str(row[3])
		pin = row[0]
		maxCode = row[2]
		msg += 'Numero de transacciones aprobadas:' + str(maxCode) + '\n'
		msg += 'PIN: ' + str(pin) + '\n'
		

	# Credentials (if needed)
	username = 'softwaresegurobanco@gmail.com'
	password = 'C0l0mb14'

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)

	db.close();
	server.quit()
