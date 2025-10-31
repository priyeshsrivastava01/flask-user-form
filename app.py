from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Database file
DB_FILE = 'users.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Phone TEXT NOT NULL,
            Designation TEXT NOT NULL,
            Company TEXT NOT NULL,
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    try:
        return sqlite3.connect(DB_FILE)
    except Exception as e:
        raise Exception(f"Database connection failed: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    conn = None
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        designation = request.form['designation']
        company = request.form['company']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO Users (Name, Email, Phone, Designation, Company)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, designation, company))
        
        conn.commit()
        flash('Form submitted successfully!', 'success')
        
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
    finally:
        if conn:
            conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')