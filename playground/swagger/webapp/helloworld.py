from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config


@view_config(
    route_name='hello',
)
def hello_world(request):
    return Response('Hello World!')


if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_swagger')

        config.add_route('hello', '/')

        config.add_route('get_dog', '/dogs/{id}')
        config.add_route('create_dog', '/dogs')

        config.scan(package='zoo')

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

