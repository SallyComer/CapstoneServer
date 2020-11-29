# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time



hostName = "localhost"
serverPort = 8080

def read_text(path):
    f = open(path)
    s = f.read()
    f.close()
    return s

def read_image(img):
    f = open(img, "rb")
    s = f.read()
    f.close()
    return s

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path.endswith(".html"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(read_text("." + self.path), "utf-8"))
        elif self.path.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            self.wfile.write(bytes(read_text("." + self.path), "utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(read_text("./index.html"), "utf-8"))
        elif self.path.endswith(".png"):
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            self.wfile.write(bytes(read_image("." + self.path)))
        elif self.path.endswith(".jpg"):
            self.send_response(200)
            self.send_header("Content-type", "image/jpg")
            self.end_headers()
            self.wfile.write(bytes(read_image("." + self.path)))
        elif self.path.endswith(".jpeg"):
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            self.wfile.write(bytes(read_image("." + self.path)))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Page not found", "utf-8"))
    def do_POST(self):
        print("handling post request")
        print(self.path)
        print(self)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
