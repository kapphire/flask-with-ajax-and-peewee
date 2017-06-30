from peewee import *

def connection():
	conn = MySQLDatabase('pythonprogramming', host = 'localhost', user = 'root', password = '')
	return conn