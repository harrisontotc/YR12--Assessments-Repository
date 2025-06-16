from flask import *
import sqlite3

app = Flask(__name__)

# Ensures the correct table is present before sending the form data

@app.route('/')
def main():
    connection = sqlite3.connect('YR12--Assessments-Repository/Website/assessdatabase.db')
    connection.commit()
    connection.close()
    return render_template('index.html')


# Pass the form data through app.py and to the database
@app.route('/', methods = ['POST'])
def send_to_database():
    votername = request.form['name']
    voterage = request.form['age']
    candidateid = request.form['candidate']
    connection = sqlite3.connect('YR12--Assessments-Repository/Website/assessdatabase.db')
    cursor = connection.cursor()
    query1 = "INSERT INTO voters (votername,voterage,candidateid) VALUES ('{n}','{a}','{c}')".format(n=votername,a=voterage,c=candidateid)
    cursor.execute(query1)
    connection.commit()
    
    return redirect(url_for('main'))

if __name__== '__main__':
    app.run(debug=True)