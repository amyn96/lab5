import socket                   # Import socket module

port = 8080                     # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ("Waiting for connection....")

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ("Got connection from", addr)
    
    filename='server.txt'
    file = open(filename, 'wb') # write 
    print('receiving data...')
    f_data = conn.recv(1024)
    file.write(f_data)            # write data to a file

    file.close()
    print('Successfully get the file!!')
    conn.close()
    s.close()