# simple-search-cgi (Archived)

  A Simple Case-Insensitive Search script written in python for your website.
  It works on Apache 2.4 servers 

# setup 

  Edit the search.py file located in cgi-bin/search.py
  You should edit two variables in order to make it works:
  
  1) search-dir
  2) server-dir 
  
  Example: If you got an Apache Server on /srv/http and you want to search files inside /srv/http/files/
    search-dir would be /srv/http/files/ while server-dir would be /files/
   
  Remember to put an ending "/" to server-dir because it will be threated as a string 
  If you're searching for apple and you find an apple.txt, withount and ending /
  the link of apple.txt will be /filesapple.txt instead of /files/apple.txt
   
  Remember to enable .py cgi on your apache configuration file and the cgi module.
