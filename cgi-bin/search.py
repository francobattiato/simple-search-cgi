#!/usr/bin/python
###########################################################################
#                                                                         #
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE                  #
#                    Version 2, December 2004                             #
#                                                                         #
# Copyright (C) 2004 Sam Hocevar                                          #
#  22 rue de Plaisance, 75014 Paris, France                               #
# Everyone is permitted to copy and distribute verbatim or modified       #
# copies of this license document, and changing it is allowed as long     #
# as the name is changed.                                                 #
#                                                                         #
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE                  #
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION       #
#                                                                         #
#  0. You just DO WHAT THE FUCK YOU WANT TO.                              #
#                                                                         #
###########################################################################

import cgi, cgitb 
import os, re

# Set your search paths: 
search_dir = "/path/to/your/system/dir/" # Where is the file located in your O.S.?
server_dir = "/path/to/your/server/dir/" # Where is the file located in the server?

# Get the filename from search.htm (?=... ), the filename is called "something"
form = cgi.FieldStorage() 
something = form.getvalue('something')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print(' <link rel="stylesheet" type="text/css" href="/search.css">')
print(" <title>Simple Search cgi</title>")
print("</head>")
print("<body>")
print('<h1> Search results for: ' + something + '</h1>')

# Search results are showed here
[print('<li><a href="' + server_dir + filename + '"><font size=5>' + filename + '</font></a><br></li>') for filename in os.listdir(search_dir) if re.search(something, filename, re.IGNORECASE)]

print('<br clear=all>')
print('<a href="/index.html"><b>Go Back</b></a>')
print('</body>')
print('</html>')
