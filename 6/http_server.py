from http.server import *
from urllib.parse import *
from search import search
import json

# ex 6, p1/p2
class Handler(BaseHTTPRequestHandler):
    """ for tests:
    http://localhost:8000/result?q=tom&f=html
    http://localhost:8000/result?q=tom&f=json
    """
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200, 'OK')
        s.send_header("Content-type", "text/html")
        s.end_headers()

        url = s.requestline.split(' ')[1]
        query_table = parse_qs(urlparse(url).query)
        print(url)
        print(query_table)

        if 'q' not in query_table:
            s.wfile.write(str.encode('no result\n'))
        else:
            res = search(query_table['q'][0])
            out = []
            print(res)

            if 'f' in query_table and query_table['f'][0] == 'json':
                s.wfile.write(str.encode(json.dumps(res)))
            elif 'f' in query_table and query_table['f'][0] == 'html':
                s.wfile.write(str.encode("<html><body>"))
                for i in res:
                    s.wfile.write(str.encode("<p>"))
                    s.wfile.write(str.encode(i[0]))
                    s.wfile.write(str.encode(" :" + str(i[1])))
                    s.wfile.write(str.encode("</p>"))
                s.wfile.write(str.encode(out))
                s.wfile.write(str.encode("</body></html>"))

httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()

# vim: set ts=4 sts=4 sw=4 :
