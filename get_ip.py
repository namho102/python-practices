import socket   #for sockets
import sys  #for exit
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print("Socket Created")
 
# host = 'www.google.com'
host = input("Enter host name: ")
 
remote_ip = socket.gethostbyname( host )
     
print ('Ip address of ' + host + ' is ' + remote_ip)