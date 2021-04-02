from socketserver import TCPServer
from handler import FileHandler

host, port = "localhost", 3000
server = TCPServer((host, port), FileHandler)
server.serve_forever()