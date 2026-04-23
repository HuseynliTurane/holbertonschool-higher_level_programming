import http.server
import json
import socketserver

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Sadə HTTP sorğu idarəedicisi"""

    def do_GET(self):
        """GET sorğularını emal edir"""

        # 1. Əsas yol (Root)
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. /data endpoint-i (JSON qaytarır)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # 3. /status endpoint-i
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. /info endpoint-i (Əlavə məlumat üçün)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # 5. Tapılmayan yollar üçün 404 xətası
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server():
    """Serveri başladır"""
    PORT = 8000
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server http://localhost:{PORT} ünvanında işləyir...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
