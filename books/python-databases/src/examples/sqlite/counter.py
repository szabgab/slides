"""
    Counter using an SQLite backend
    --list            list all the counters
    --start name     creates the counter for 'name'
    name             counts for 'name'
"""

import sys
import os
import argparse
import sqlite3

database_file = "counter.db"

def list_counters(crs):
    print('List counters:')
    for name, count in crs.execute("SELECT name, count FROM counters"):
        print(f"{name}: {count}")

def get_counter(crs, name):
    crs.execute("SELECT count FROM counters WHERE name = ?", (name,))
    line = crs.fetchone()
    if line is None:
        return None
    return line[0]


def increase_counter(conn, crs, name):
    counter = get_counter(crs, name)
    if counter is None:
        print(f"Invalid counter name '{name}' use the --start flag to start a new counter")
        return

    counter += 1
    crs.execute("UPDATE counters SET count=? WHERE name = ?", (counter, name))
    conn.commit()
    print(f"{name} {counter}")

def start_counter(conn, crs, name):
    counter = get_counter(crs, name)
    if counter is not None:
        print(f"Counter {name} already exists")
        return

    try:
        crs.execute("INSERT INTO counters (name, count) VALUES(?, ?)", (name, 0))
        conn.commit()
    except sqlite3.IntegrityError as err:
        print(f"Name '{name}' already exists")

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--start', action='store_true')
    parser.add_argument('name', nargs="?")
    args = parser.parse_args()
    if args.name is None and not args.list:
        parser.print_help()
        exit()
    return args

def main():
    args = get_arguments()

    with sqlite3.connect(database_file) as conn:
        crs = conn.cursor()
        try:
            crs.execute('''CREATE TABLE counters (
              id PRIMARY KEY,
              name VARCRCHAR(100) UNIQUE NOT NULL,
              count INTEGER NOT NULL
              )''')
        except sqlite3.OperationalError as err:
            pass
            #print(f'sqlite error: {err.args[0]}')

        if args.list:
            list_counters(crs)
            return

        if args.start  and args.name:
            start_counter(conn, crs, args.name)
            return

        if args.name:
            increase_counter(conn, crs, args.name)
            return

main()

#print "TODO get the value of 'name' from the database"
# if it was not there then add


#try:
#  c.execute('''INSERT INTO companies (name) VALUES ('Stonehenge')''')
#except sqlite3.IntegrityError as e:
#  print 'sqlite error: ', e.args[0] # column name is not unique

#conn.commit()

#conn.close()

#print "done"

