#!/usr/bin/python

import cgi, cgitb
import os
import Cookie
cgitb.enable()

def getSalt():
  return "St"
 
def getClientCookie():
  idClient="0"
  if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    try:
      idClient=c['idusuario'].value
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
    am= str(amount)
    amount2 =am[:am.find(".")]
    random=codTran[codTran.find("-")+1:]
    cod2= long(pin1)+long(pin2) + (long(amount2) * (long(random)+61))
    codTran2 =  str(cod2)+'-'+str(random);
    return codTran == codTran2
       
    