import socket

# real test with google.com
HOST = "www.google.com"
PORT = 80

# test with tcp_server.py
HOST = "0.0.0.0"
PORT = 9998

# create client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client.connect((HOST, PORT))

# send arbitrary data
# client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")
client.sendall(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response.decode('utf-8'))

client.close()


# Result
# ---
# HTTP/1.1 301 Moved Permanently
# Location: http://www.google.com/
# Content-Type: text/html; charset=UTF-8
# Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-IwcvFsBAkJw2QIzyKXuEYg' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
# Date: Mon, 24 Aug 2026 15:47:58 GMT
# Expires: Wed, 23 Sep 2026 15:47:58 GMT
# Cache-Control: public, max-age=2592000
# Server: gws
# Content-Length: 219
# X-XSS-Protection: 0
# X-Frame-Options: SAMEORIGIN

# <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
# <TITLE>301 Moved</TITLE></HEAD><BODY>
# <H1>301 Moved</H1>
# The document has moved
# <A HREF="http://www.google.com/">here</A>.
# </BODY></HTML>