from pyramid.view import view_config
from wsgiref.simple_server import make_server
from pyramid.config import Configurator


@view_config(route_name='root', renderer='index.jinja2', request_method='GET')
@view_config(route_name='index', renderer='index.jinja2', request_method='GET')
@view_config(route_name='aboutme', renderer='about/aboutme.jinja2', request_method='GET')
def exists_page(request):
    return {}


if __name__ == "__main__":
    config = Configurator()
    config.add_route(name='index', path='/index.html')
    config.add_route(name='root', path='/')
    config.add_route(name='aboutme', path='/about/aboutme.html')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('templates', name='.jinja2')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()

