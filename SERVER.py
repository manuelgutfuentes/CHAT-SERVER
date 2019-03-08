import socket

PORT = 9089
IP = "10.108.33.18"
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket):
    print(clientsocket)
    condition = True
    while condition:

        out = input("(S) Type a message: ")
        outbox = str.encode(out)
        clientsocket.send(outbox)
        inbox = clientsocket.recv(2048).decode("utf-8")
        print("CLIENT said: ", inbox)
        if out.lower() == "colgar" or inbox.lower() == "colgar":
            condition = False

    clientsocket.close()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)