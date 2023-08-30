#!/usr/bin/python3
"""
This script takes an argument and displays all values of the staes
table that match the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    query = """ SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC """.format(sys.argv[4])

    cur.execute(query)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
