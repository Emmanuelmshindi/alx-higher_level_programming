#!/usr/bin/python3
"""
This script takes in the name of a state as argument and lists all cities
of that state.Results must be sorted in ascending order by cities.id
"""
import MySQLdb
import sys

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

        query = """SELECT cities.name
                   FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC"""

        cur.execute(query, (state_name,))

        query_rows = cur.fetchall()

        print(", ".join([city[0] for city in query_rows]))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
