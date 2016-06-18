#!/usr/bin/python
import smtplib
import MySQLdb

def sendmail(clientId):
	fromaddr = 'softwaresegurobanco@gmail.com'
	
	#db = connectDB()
	db = MySQLdb.connect("localhost","root","samurai","banksafe")
	cursor = db.cursor()
	#if conn.is_connected():
	#    print('Connected to MySQL database')
	sql = "SELECT * FROM client WHERE idClient = '%d'" % (clientId)
	cursor.execute(sql)
	# fetch all of the rows from the query
	data = cursor.fetchall()

	msg = 'Su registro ha sido aprobado, bienvenido a BankSafe!!\n\n Ahora cuenta con los siguientes codigos de transaccion:\n\n'
	for row in data:
		toaddrs = str(row[3])
		consec = row[6]
		maxCode = row[7]
		while consec <= maxCode:
			msg += str(clientId) + '-' + str(consec) + '\n'
			consec += 1

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
