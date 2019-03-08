import socket

IP = "10.108.33.18"
PORT = 9089

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
    print("conexión establecida")
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

condition = True
while condition:
    inbox = s.recv(2048).decode("utf-8")
    print("SERVER said: ", inbox)
    out = input("(C) Type a message: ")
    outbox = str.encode(out)
    s.send(outbox)
    if out.lower() == "colgar" or inbox.lower() == "colgar":
        condition = False

s.close()