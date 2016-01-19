#!/usr/bin/env python

# Copyright 2011 Pointlessprogramming
# taken from 
# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# using this for CMPUT404 Lab2, will be taken down immediately upon request

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()

