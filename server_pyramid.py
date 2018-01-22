#!/usr/bin/python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import json
import sqlite3

# Accepts a JSON POST request.
# Requires two fields in the payload of the POST.  A "title" and "body" field.
# Returns a blank response back to the caller.  This is required by the Pyramid framework.
def post(request):
	print("the post endpoint has been called with POST!!!.")
	conn = sqlite3.connect('blog.db')
	c = conn.cursor()

	resp = request.get_response
#	print(resp)
	body = request.body
#	print(body)
	json = request.json_body
#	print(json)
	titleIn = json["title"]
	bodyIn = json["body"]
#	print("title " + titleIn)
#	print("body" + bodyIn)

	c.execute("INSERT INTO posts (title, body) VALUES (?, ?)", (titleIn, bodyIn,))
	conn.commit()
	conn.close()
	request.response.text = 'OK'
	return request.response

# Accepts GET type requests on this endpoint.
# Returns a JSON object with an array of tuples one tuple per row in the table.
def posts(request):
	print("POSTS has been called with a GET command.")
	conn = sqlite3.connect('blog.db')
	c = conn.cursor()
	c.execute('SELECT * FROM posts')
	results = c.fetchall()

	posts_as_dict = []

	for entry in results:
		entry_as_dict = {
			"id": entry[0],
			"title" : entry[1],
			"body" : entry[2]
		}
		posts_as_dict.append(entry_as_dict)

	conn.close()
	return posts_as_dict

if __name__ == '__main__':
	print("server_pyramid.py is running...")
	with Configurator() as config:
		config.add_route('post', '/post/')
		config.add_view(post, route_name='post', request_method="POST", renderer='json')

		config.add_route('posts', '/posts/')
		config.add_view(posts, route_name='posts', request_method="GET", renderer='json')

		app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 9797, app)
	server.serve_forever()