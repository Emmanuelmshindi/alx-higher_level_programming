#!/usr/bin/python3
"""
This script takes in the name of a state as argument and lists all cities
of that state.Results must be sorted in ascending order by cities.id
"""
import MySQLdb
import sys

if __name__ = '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id = cities.state_id 
            WHERE states.name = '{}' ORDER BY cities.id ASC".format(state_name))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
