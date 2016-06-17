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
  