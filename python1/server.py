import socket
import threading

server = socket.socket()

server.bind(("localhost", 6767))
server.listen()

print("Server is listening on port 6767...")

connections = 0
def handle_client(client):
    while True:
        msg = client.recv(1024)

        if not msg:
            break

        print(f"Received message: {msg.decode()}") #Print the received message
        print(threading.current_thread().name) #Print the name of the current thread

        client.send(msg) #Echo the message back to the client

    client.close()

lock = threading.Lock()

while True:
    client, addr = server.accept()
    with lock:
        connections += 1
    
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()