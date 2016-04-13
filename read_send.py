#Socket client example in python
 
import socket   #for sockets
import sys  #for exit
 
#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
print('Socket Created')
 
host = input('Enter host name: ');
port = 80;
 
remote_ip = socket.gethostbyname( host )
 
#Connect to remote server
s.connect((remote_ip , port))
 
print('Socket Connected to ' + host + ' on ip ' + remote_ip)
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
s.sendall(bytes(message, 'UTF-8'))
 
print('Message send successfully')
 
#Now receive data
reply = s.recv(4096)
 
print (reply)