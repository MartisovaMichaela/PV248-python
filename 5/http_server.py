from http.server import *

# part 1 & 2

class Handler(BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200, 'OK')
        s.send_header("Content-type", "text/html")
        s.end_headers()

        filename = s.requestline.split(' ')[1]
        if filename != '/':
            try:
                f = open(filename.strip('/'), 'r')
                txt = f.read()
                s.wfile.write(str.encode(txt))
            except:
                s.wfile.write(str.encode("failed to open file"))
        else:
            s.wfile.write(str.encode("static test"))

httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()

# vim: set ts=4 sts=4 sw=4 :
