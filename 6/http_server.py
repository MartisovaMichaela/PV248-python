from http.server import *
from urllib.parse import *
from search import search
import json

# ex 6, p1/p2/p3
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

        if len(query_table) == 0:
            present_form(s)
            pass
        else:
            if 'q' not in query_table:
                s.wfile.write(str.encode('no result\n'))
                return

            res = search(query_table['q'][0])
            print(res)

            if 'f' in query_table and query_table['f'][0] == 'json':
                present_json(s, res)
            elif 'f' in query_table and query_table['f'][0] == 'html':
                present_html(s, res)


def present_form(state):
    form = """
<!DOCTYPE html>
<html>
<body>
<form action="result">
  Search string:<br>
  <input type="text" name="q" value="mozart"><br>
  Format:<br>
  <input type="text" name="f" value="html"><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
"""
    state.wfile.write(str.encode(form))


def present_json(state, data):
    state.wfile.write(str.encode(json.dumps(data)))


def present_html(state, data):
    out = "<html><body>%s</html></body>"
    lines = []
    for i in data:
        line = "<p>%s: %s</p>" % (i[0], str(i[1]))
        lines.append(line)
    state.wfile.write(str.encode('\n'.join(lines)))


httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()

# vim: set ts=4 sts=4 sw=4 :
