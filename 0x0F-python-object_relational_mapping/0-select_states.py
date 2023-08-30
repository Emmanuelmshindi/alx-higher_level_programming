#!/usr/bin/python3

"""
This script lists all states in a MySQL database from a table called 'states'
The MySQL username, password and database name are passed as arguments in the
command line.
The results are sorted by id in ascending order and printed out on the
command line.The module MySQLdb is used to connect to a MySQL server on
localhost on port 3306.A select statement is used to fetch all rows from the
states table, alongside the fetchall() function, and prints the output in
the format '(id, name)'
Usage:
    ./0-select_states.py username password mydatabase
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=sys.argv[1], 
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
