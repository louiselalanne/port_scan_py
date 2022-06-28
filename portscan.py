#!/usr/bin/python
#---------PORT SCAN------------ 
from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   ip = gethostbyname(target)
   print ('Starting scan on host: ', ip)
   
   for port in range (1, 65535):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((ip, port))
      if(conn == 0) :
         print ('Port %d: OPEN' % (port,))
      s.close()
print('Time taken:', time.time() - startTime)
