import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "192.168.43.50"
port = 8080                     # Reserve a port
s.connect((host, port))
print ("... Connected!\n")

filename = input(str("Enter file name : "))   # enter file name
file = open(filename,'rb')  #Read
print('sending data...')
data = file.read(1024)   # read data file
s.send(data)

print("Done sending")
file.close()
s.close()
print("connection closed") 