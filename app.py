from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'flask-secret-key-2024')

# Check if running on Railway (has DATABASE_URL)
if os.getenv('DATABASE_URL'):
    # Use PostgreSQL for Railway
    import psycopg2
    from urllib.parse import urlparse
    
    def get_db_connection():
        url = urlparse(os.getenv('DATABASE_URL'))
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        # Create table if not exists
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                ID SERIAL PRIMARY KEY,
                Name VARCHAR(100) NOT NULL,
                Email VARCHAR(100) NOT NULL,
                Phone VARCHAR(20) NOT NULL,
                Designation VARCHAR(100) NOT NULL,
                Company VARCHAR(100) NOT NULL,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
        return conn
else:
    # Use SQL Server for local development
    import pyodbc
    
    DB_CONFIG = {
        'server': os.getenv('DB_SERVER', 'localhost\\SQLEXPRESS'),
        'database': os.getenv('DB_NAME', 'Practice DB'),
        'username': os.getenv('DB_USERNAME', 'sa'),
        'password': os.getenv('DB_PASSWORD', 'Sanju@123456'),
        'driver': '{ODBC Driver 17 for SQL Server}'
    }
    
    def get_db_connection():
        try:
            conn_str = f"DRIVER={DB_CONFIG['driver']};SERVER={DB_CONFIG['server']};DATABASE={DB_CONFIG['database']};UID={DB_CONFIG['username']};PWD={DB_CONFIG['password']}"
            return pyodbc.connect(conn_str)
        except pyodbc.Error as e:
            raise Exception(f"Database connection failed: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users ORDER BY CreatedAt DESC')
    users = cursor.fetchall()
    conn.close()
    return render_template('admin.html', users=users)

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
        
        if os.getenv('DATABASE_URL'):
            # PostgreSQL syntax
            cursor.execute("""
                INSERT INTO Users (Name, Email, Phone, Designation, Company)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, email, phone, designation, company))
        else:
            # SQL Server syntax
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
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')