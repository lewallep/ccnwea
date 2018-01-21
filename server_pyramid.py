#!/usr/bin/python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import json

import sqlite3

def post(request):
	print("the post endpoint has been called with POST!!!.")
	conn = sqlite3.connect('blog.db')
	c = conn.cursor()

	resp = request.get_response
	print(resp)
	body = request.body
	print(body)
	json = request.json_body
	print(json)
	titleIn = json["title"]
	bodyIn = json["body"]
	print("title " + titleIn)
	print("body" + bodyIn)

	c.execute("INSERT INTO posts (title, body) VALUES (?, ?)", (titleIn, bodyIn,))
	conn.commit()
	conn.close()
	return Response("Placeholder Response")

def posts(request):
	print("POSTS has been called with a GET command.")
	c = sqlite3.connect('blog.db').cursor()
	c.execute('SELECT name FROM sqlite_master WHERE type="table"')
	print(c.fetchall())

	c.execute('SELECT * FROM posts')
	print(c.fetchall())

	c.execute("PRAGMA TABLE_INFO({})".format("posts"))
	print(c.fetchall())
	c.close()
	
	return {'content':'Hello!'}

if __name__ == '__main__':
	print("server_pyramid.py is running...")
	with Configurator() as config:
		config.add_route('post', '/post/')
		config.add_view(post, route_name='post', request_method="POST")

		config.add_route('posts', '/posts/')
		config.add_view(posts, route_name='posts', request_method="GET", renderer='json')

		app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 9797, app)
	server.serve_forever()