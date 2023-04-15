#!/usr/bin/python3
"""
This script lists all states in a MySQL database from a table called 'states',
with a name starting with N.
The MySQL username, password and database name are passed as arguments in the
command line.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
