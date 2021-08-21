#!/usr/bin/env python
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
# Set up basic http web server to run from CWD
os.chdir('.')
# Set up server object to listen on port 80
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# Start up server at http://localhost
server_object.serve_forever()
