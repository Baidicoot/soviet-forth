from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs
from datetime import datetime

def addDefn(addr, body):
    parsed = parse_qs(body)
    scope = json.load(open("scope.json", "r"))

    name = parsed["name"][0]
    defn = parsed["defn"]

    scope[name] = defn
    with open("scope.json", "w") as file:
        json.dump(scope, file)
    with open("defns.log.txt", "a") as file:
        file.write(addr + ", " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ": " + json.dumps({name:defn}) + "\n")

class ScopeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("scope.json", "rb") as file:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        addDefn(self.client_address[0], body.decode("utf-8"))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Good POST')

httpd = HTTPServer(('192.168.1.29', 8080), ScopeServer)
httpd.serve_forever()