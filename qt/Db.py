import json
import sqlite3
import Queue
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('db.conf')

dbName = config.get('db', 'name')
dbUser = config.get('db', 'user')
dbPassword = config.get('db', 'password')