import falcon, json
from falcon_cors import CORS
from alignements_backend.notion import Notion
from alignements_backend.variable import Variable
from alignements_backend.middlewares import RequireJSON, JSONTranslator
from urllib.parse import unquote


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
        uri = unquote(req.params['uri']).decode('utf8')
        uris = Notion.get_uris(uri)
        if not uri:
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_200
            req.context['result'] = uris


class VariableResource:
    def on_get(self, req, resp, var_name):
        var = Variable.get_from_id(var_name)
        if not var:
            resp.status = falcon.HTTP_404
        else:
            resp.status = falcon.HTTP_200
            req.context['result'] = json.loads(var)


public_cors = CORS(allow_all_origins=True, allow_all_headers=True,
        allow_all_methods=True, allow_credentials_all_origins=True)
app = falcon.API(
    middleware=[
    RequireJSON(),
    JSONTranslator(),
    public_cors.middleware
    ]
)

notions = NotionsResource()
variables = VariableResource()
app.add_route('/notions/', notions)
app.add_route('/variables/{var_name}/', VariableResource())
app.add_route('/variables/{var_name}', VariableResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
