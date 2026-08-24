import socket
import threading

IP = "0.0.0.0"
PORT = 9998

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((IP, PORT))
  server.listen(5) # connection MAX Limit = 5

  print(f"[*] Listening on {IP}:{PORT}")

  while True:
    client, address = server.accept() # client = client socket, address = detail info related to remote connection
    print(f"[*] Accepted connection from {address[0]}:{address[1]}")
    
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

def handle_client(client_socket):
  with client_socket as socket:
    request = socket.recv(1024) # 1024 bytes
    print(f"[*] Received : {request.decode('utf-8')}")
    socket.send(b"ACKKK")


if __name__ == "__main__":
  main()


# Extending these codes, we can develop netcat program or TCP Proxy features