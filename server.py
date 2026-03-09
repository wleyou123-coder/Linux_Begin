#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"  # слушать на всех интерфейсах
port = 8000

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Server running on http://{host}:{port}")
server.serve_forever()

