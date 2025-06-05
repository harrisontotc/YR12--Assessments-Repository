from flask import Flask, g, render_template
import sqlite3
import os

DATABASE = r"G:\My Drive\Year 12 Programming Assessment Files\YR12--Assessments-Repository\Website\Code\SQL\database.db"

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    #home page
    return render_template("G:\My Drive\Year 12 Programming Assessment Files\YR12--Assessments-Repository\Website\Code\HTML\index.html")

if __name__ == '__main__':
    app.run(debug=True)