from flask import Flask, request, render_template, redirect, url_for
import os
import sqlite3

app = Flask(__name__)

dbfile = "app.db"
@app.route("/", methods=['GET'])
def main_get():
    tasks = []
    try:
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        sql = '''SELECT id, title FROM tasks'''
        for task in c.execute(sql):
            tasks.append({
                "id"    : task[0],
                "title" : task[1],
            })
        conn.close()
    except Exception as err:
        pass

    return render_template('main.html', tasks=tasks)

@app.route("/", methods=['POST'])
def main_post():
    title = request.form['title']
    if title:
        try:
            conn = sqlite3.connect(dbfile)
            c = conn.cursor()
            c.execute('''INSERT INTO tasks (title) VALUES (?)''', (title,))
            conn.commit()
            conn.close()
        except Exception as err:
            pass
        # print('sqlite error: ', err.args[0])

        return redirect(url_for('main_get'))
    return render_template('error.html')


def create_db(dbfile):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()

    try:
        c.execute('''CREATE TABLE tasks (
            id         PRIMARY KEY,
            title      VARCRCHAR(100) UNIQUE NOT NULL,
            done       BOOLEAN DEFAULT false
            )
        ''')
    except sqlite3.OperationalError as e:
        print('sqlite error:', e.args[0])

    conn.commit()
    conn.close()

if not os.path.exists(dbfile):
    create_db(dbfile)

