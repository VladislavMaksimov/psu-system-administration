from socketserver import ThreadingTCPServer
from handler import FileHandler

host, port = "localhost", 3000
server = ThreadingTCPServer((host, port), FileHandler)
server.serve_forever()