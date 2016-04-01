import falcon, json
from alignements_backend.notion import Notion
from alignements_backend.middlewares import RequireJSON, JSONTranslator

class NotionsResource:
    def on_post(self, req, resp):
        if not isinstance(req.context['doc'], list):
            raise falcon.HTTPBadRequest('Bad JSON format',
                'A list is needed')
        if any(map(lambda v: not isinstance(v, str), req.context['doc'])):
            raise falcon.HTTPBadRequest('Bad JSON format',
                'Only strings are accepted')
        n = Notion(*req.context['doc'])
        resp.status = falcon.HTTP_201
        resp.location = '/notions?uri=%s' % n.uris[0]

    def on_get(self, req, resp):
        if not 'uri' in req.params:
            raise falcon.HTTPBadRequest('uri param needed')
        uri = req.params['uri']
        uris = Notion.get_uris(uri)
        if not uri:
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_200
            req.context['result'] = uris

app = falcon.API(
    middleware=[
    RequireJSON(),
    JSONTranslator()
    ]
)

notions = NotionsResource()
app.add_route('/notions/', notions)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
