import socket

client = socket.socket() #Create a TCP socket object
client.connect(("localhost", 6767))
while True:
    msg = input("Enter a message > ")
    client.send(msg.encode()) #Send the message to the server
    response = client.recv(1024)
    print(response.decode()) #Print the response from the server
