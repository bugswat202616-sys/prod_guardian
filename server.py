import http.server
import socketserver

# Define the port to serve on
PORT = 8000

# Custom request handler to intercept specific routes
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Intercept the specific path and issue a 302 Redirect
        if self.path == '/verify.sh':
            self.send_response(302)
            self.send_header('Location', 'http://local.dared.in/verify.sh')
            self.end_headers()
        else:
            # Fall back to standard file serving for all other paths
            super().do_GET()

# Create the TCP server and bind it to the custom handler
with socketserver.TCPServer(("", PORT), CustomRequestHandler) as httpd:
    print(f"🚀 Serving files locally at http://localhost:{PORT}")
    try:
        # Keep the server running until manually stopped (Ctrl+C)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
