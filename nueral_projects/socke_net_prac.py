import socket

# which socket do you want
# tcp(accurate) or udp(faster but risk of losing data)?
# which ip are we going to connect to?
# Which port are we going to connect to port(443, 80)
# udp SOCK_DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 55555))
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()