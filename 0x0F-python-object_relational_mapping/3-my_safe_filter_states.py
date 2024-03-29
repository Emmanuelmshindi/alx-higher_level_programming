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

    try:

        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)

        cur = db.cursor()

        query = """SELECT * FROM states
                   WHERE name = %s
                   ORDER BY id ASC"""

        cur.execute(query, (state_name,))

        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
