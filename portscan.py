#!/usr/bin/python
#---------PORT SCAN------------

import socket, sys

for port in range(1,65535):
  var = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  if var.connect_ex((sys.argv[1], port)) == 0:
    print "Port ",port, "Open"
    var.close()
