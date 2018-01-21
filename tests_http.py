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

def clearTable():
	print("clearTable() has been called")


if __name__ == '__main__':
	postOne()
	print("end of program.")