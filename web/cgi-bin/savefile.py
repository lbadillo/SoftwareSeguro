#!/usr/bin/python
import MySQLdb
import cgi, cgitb
import os
import constants 
import subprocess


cgitb.enable()

idClient = constants.getClientCookie()
respon ="Usuario No Registrado"
form = cgi.FieldStorage()
fileitem = form['filename']
respon="Usuario no registrado"
constants.getHeaderHtml( "Transacciones Batch")
if idClient != "0":
  if fileitem.filename:
    
    fn = os.path.basename(fileitem.filename.replace("\\","/"))
    open ('/var/www/cgi-bin/' + fn, 'wb' ).write (fileitem.file.read())
    p = subprocess.Popen(['chmod','777', '/var/www/cgi-bin/' + fn], stdout=subprocess.PIPE)
    out, err = p.communicate()
    if err is None:
      p2 = subprocess.Popen(['./main',idClient], stdout=subprocess.PIPE)
      out2, err2 = p2.communicate()
      if err2 is None:
	
	respon = 'Transacciones Generadas Satisfactoriamente'
      else:
	respon = err2
    else:
      respon = err
  
print '<div class="well">' 
print '<h4> %s</h4>' % (respon) 
print '</div>'
print "<a href = 'clientoptions.py'> Volver a opciones </a>"
constants.getFooterHtml()   
print '</body>'
print '</html>'
