#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect("sample.db")
c = conn.cursor()

# use the database here

conn.close()
