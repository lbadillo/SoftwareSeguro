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
