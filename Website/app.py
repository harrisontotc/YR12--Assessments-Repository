from flask import Flask, request, render_template, request, redirect, url_for
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'G:\My Drive\Year 12 Programming Assessment Files\YR12--Assessments-Repository\Website\database.db')
conn = sqlite3.connect(db_path)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if request.method == 'POST':
        voter_name = request.form['name']
        voter_age = request.form['age']
        candidate_id = request.form['candidate']

        cursor.execute('''
                       INSERT INTO voters (VoterName, VoterAge, CandidateID)
                       VALUES (?,?,?)
                       ''', (voter_name, voter_age, candidate_id))
        
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.execute('SELECT CandidateID, CandidateName FROM candidates')
    candidates = cursor.fetchall()
    conn.close()

    return render_template('index.html', candidates=candidates)
