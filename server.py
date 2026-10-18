import http.server
import socketserver

# Define the port to serve on
PORT = 8000

# Set up the standard request handler for serving files
Handler = http.server.SimpleHTTPRequestHandler

# Create the TCP server and bind it to the port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Serving files locally at http://localhost:{PORT}")
    try:
        # Keep the server running until manually stopped (Ctrl+C)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
