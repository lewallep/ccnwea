#!/usr/bin/python
import json
import requests
import sqlite3

def postOne():
	headers = {"contentType" : "application/json"}
	payload = { "title":"Post Title 01", "body":"This is the first test post I have made with my test driver program." }
	req = requests.post("http://192.168.56.101:9797/post/", data=json.dumps(payload), headers=headers)

	print(req.status_code)
	print(req.text)

#Deletes all of the entries from the table.
def clearTable():
	print("clearTable() has been called")
	conn = sqlite3.connect('blog.db')
	c = conn.cursor()
	c.execute("DELETE FROM posts")
	conn.close()

if __name__ == '__main__':
	postOne()
	clearTable()
	print("end of program.")