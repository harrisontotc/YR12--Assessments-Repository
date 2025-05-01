from flask import Flask, g, render_template
import sqlite3
import os

DATABASE = r"G:\My Drive\Year 12 Programming Assessment Files\YR12--Assessments-Repository\Mini Practice Projects\PracticeProject1_WebsiteWithFlask\database.db"

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
    sql = """SELECT Bikes.BikeID,Makers.Name,Bikes.Model,Bikes.ImagURL
             FROM Bikes
             JOIN Makers ON Makers.MakerID=Bikes.MakerID;"""
    results = query_db(sql)
    return render_template("layout.html")

@app.route("/bike/<int:id>")
def bike(id):
    sql = """SELECT * FROM Bikes 
             JOIN Makers ON Makers.MakerID = Bikes.MakerID
             WHERE Bikes.BikeID = ?;"""
    result = query_db(sql, (id,), True)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)



