#!/usr/bin/python

import cgi, cgitb
import os
import Cookie
from Crypto.Hash import SHA256
cgitb.enable()

def getSalt():
  return "St"

def getTimeCookie():
  return 5
  
def generateSHA(value):
    m= SHA256.new()
    m.update(str(value))
    return m.hexdigest()
  
  
def setClientCookie(idClient):
    c=Cookie.SimpleCookie()
    c['idusuario']=idClient
    c['idusuario']['expires']=getTimeCookie()
    c['sessionclient']= generateSHA(idClient)
    c['sessionclient']['expires']=getTimeCookie()
    print c
    print "Location: clientoptions.py\r\n"

def setEmployeeCookie(idEmployee):
    c=Cookie.SimpleCookie()
    c['idemployee']=idEmployee
    c['idemployee']['expires']=getTimeCookie()
    c['sessionemployee']= generateSHA(idEmployee)
    c['sessionemployee']['expires']=getTimeCookie()
    print c 
    print "Location: empmenu.py\r\n" 
    
def getClientCookie():
  idClient="0"
  if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    try:
      idClient=c['idusuario'].value
      valor=c['sessionclient'].value
      if(valor==generateSHA(idClient)):
	  c['idusuario']['expires']=getTimeCookie()
	  c['sessionclient']['expires']=getTimeCookie()
	  print c 
      else:
	idClient['0']
    except KeyError:
      idClient="0"
  return idClient  
  
def getEmployeeCookie():
  idClient="0"
  if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    try:
      idClient=c['idemployee'].value
      valor=c['sessionemployee'].value
      if(valor==generateSHA(idClient)):
	  c['idemployee']['expires']=getTimeCookie()
	  c['sessionemployee']['expires']=getTimeCookie()
	  print c 
      else:
	idClient['0']
    except KeyError:
      idClient="0"
  return idClient  
  
def getHeaderHtml(title):
  print "Content-type: text/html\r\n\r\n";
  print '<html>'
  print '<head>'
  print '<link rel="stylesheet" href="../assets/css/bootstrap.min.css">'
  print '<link rel="stylesheet" href="../assets/css/styles.css">'
  print '<title>Bank Safe</title>'
  print '</head>'
  print '<body>'
  print '<nav class="navbar navbar-fixed-top navbar-inverse" role="navigation">'
  print	'  <div class="container-fluid">'
  print '   <div class="navbar-header">'
  print '     <a class="navbar-brand" href="#">SafeBank</a>'
  print '   </div>'
  print '  </div>'
  print '  </nav>'
  print '<div class="container-fluid">'
  print '  <div class="row">'
  print '    <div class="col-sm-12">'
  print '	<div class="page-header">'
  print'	  <h1>%s </h1>' %title
  print'	</div>'
  print'    </div>'
  print'  </div>'
  
def getFooterHtml():
  print '</div>'
  
def getPinClient(correo):
    total=0;
    i=1
    listcorreo=list(correo)
    size=len(listcorreo)
    for letter in listcorreo:
        total= (i*ord(letter))+total+size;
        i=i+1
    total=total*total    
    total= total % 999999999
    return total

def testToken(pin1,pin2, codTran, amount):
    try:
      am= str(amount)
      amount2 =am[:am.find(".")]
      random=codTran[codTran.find("-")+1:]
      cod2= long(pin1)+long(pin2) + (long(amount2) * (long(random)+61))
      codTran2 =  str(cod2)+'-'+str(random);
      return codTran == codTran2
    except:
      return False
       
    