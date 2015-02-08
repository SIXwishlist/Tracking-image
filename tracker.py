#!/usr/bin/python
import cgi
import os
import time

def currentTime():
    return time.strftime("%H:%M:%S")+" "+time.strftime("%d/%m/%Y")

form = cgi.FieldStorage()

with open(".log", "a") as logfile:
    logfile.write(currentTime())
    logfile.write(" - id: "+form.getvalue('id'))
    for p in os.environ.keys():
        logfile.write(", "+p+": "+os.environ[p])
    logfile.write("\n")

print "Content-type: image/png\n"
print open("logo.png", "rb").read()
