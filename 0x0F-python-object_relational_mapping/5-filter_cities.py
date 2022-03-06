#!/usr/bin/python3

"""
    a script that takes in the name of a state as
    an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )

    cur = db.cursor()
    sql_input = "SELECT cities.name FROM states\
                INNER JOIN cities ON states.id = \
                cities.state_id WHERE states.name = \
                %s ORDER BY cities.id ASC"
    cur.execute(sql_input, (sys.argv[4],))
    data = cur.fetchall()

    print(', '.join(i[0] for i in data))

    cur.close()
    db.close()
