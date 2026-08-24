import socket

HOST = "127.0.0.1"
PORT = 9997

# create client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP : datagram / connectionless protocol

# send arbitrary data
client.sendto(b"AAABBBCCC", (HOST, PORT))

# receive data
data, address = client.recvfrom(4096)

print(data.decode('utf-8'))
print(address.decode('utf-8'))

client.close()
