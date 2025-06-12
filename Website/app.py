from flask import *
import sqlite3

app = Flask(__name__)

#Ensures the correct table is present before sending the form data

@app.route('/', methods=['POST'])
def main():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS voters (
            VoterID INTEGER PRIMARY KEY AUTOINCREMENT,
            VoterName TEXT
            VoterAge INTEGER
            CandidateID INTEGER REFERENCES candidates(CandidateID)
    )'''


    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    return render_template('/index.html')


# Pass the form data through app.py and to the database
@app.route('/', methods = ['POST'])
def database():
    votername = request.form['name']
    voterage = request.form['age']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query1 = "INSERT INTO database (name,age) VALUES ('{n}','{a}')".format(n=votername,a=voterage)
    cursor.execute(query1)
    connection.commit()

    return redirect("/result?name=" + votername)


if __name__== '__main__':
    app.run(debug=True)