#!/usr/bin/python3
"""
This script takes an argument and displays all values of the staes
table that match the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

    cur = db.cursor()

    cur.execute("TRUNCATE TABLE states")

    cur.execute(open("0-select_states.sql", "r").read())

    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
