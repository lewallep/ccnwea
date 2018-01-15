#!/usr/bin/python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
	return Response('Hello %(name)s!' % request.matchdict + 'adding a suffix')

def post_resp(request):
	print("inside post_resp.")
	print(request.method)
	#print(request.headers['host_info'])

	for value in request.headers:
		print(value)
	print('\n')
	print(request)
	print(request.headers['accept'])
	
	return Response('Hello ')

if __name__ == '__main__':
	with Configurator() as config:
		config.add_route('hello', '/hello/{name}')
		config.add_view(hello_world, route_name='hello')
		config.add_route('posting', '/posting/', request_method="POST")
		config.add_view(post_resp, route_name='posting')
		app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 9797, app)
	server.serve_forever()