import sqlite3
import re

class DBReader(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)
        def regexp(expr, item):
            r = re.compile(expr)
            return r.match(item) is not None
        self.connection.create_function("regexp", 2, regexp)
        self.cursor = self.connection.cursor()

    def __call__(self, command, *args):
        command = '%s;' % command
        self.cursor.execute(command, args)

        if command.startswith('SELECT'):
            return self.cursor.fetchall()
        else:
            return []

    def execute_many(self, command, params):
        return self.cursor.executemany(command, params)

    def execute_script(self, script):
        return self.cursor.executescript(script)

    def query(self, command, *args):
        return self(command, *args)

    def close(self):
        self.connection.close()