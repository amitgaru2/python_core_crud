import base_dir
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from src.modules.connection import DBConnection
from src.modules.person import Person


class HttpHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):
        path = self.path.split('/')
        if path[1] == 'person' and path[2].isdigit():
            self._set_response()

            # db connection
            conn = DBConnection(select_db=2)
            conn.connect()
            _person = Person(conn) 


            resp = Person.get_dict_of_query_result(_person.read(id=path[2]).fetchone())
            self.wfile.write(json.dumps(resp, sort_keys=True).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=HttpHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()