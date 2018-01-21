#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('blog.db')
c = conn.cursor()

def basicExecutes():
	c.execute('SELECT name FROM sqlite_master WHERE type="table"')
	print(c.fetchall())

	c.execute('SELECT * FROM posts')
	print(c.fetchall())

	c.execute("PRAGMA TABLE_INFO({})".format("posts"))
	print(c.fetchall())

	conn.close()

x = "Reversing a string!!!"
print(x[::-1])

if __name__ == '__main__':
	basicExecutes()