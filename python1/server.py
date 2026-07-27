import socket

server = socket.socket() #Create a TCP socket object
server.bind(("localhost", 6767))

server.listen()
print("Server is listening on port 6767...")
client, addr = server.accept() #Accept a connection from a client
#.accept() is a blocking function, it pause execution until a client connects to the server
print(f"Connection from {addr} has been established!")

while True:
    message = client.recv(1024) #Receive a message from the client

    if not message:
        break

    client.send(message) #Echo the message back to the client

client.close() #Close the connection with the client