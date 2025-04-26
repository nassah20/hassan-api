from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host='your_database_host', 
        database='hassanDB' 
        user='root', 
        password=''  
    )

# Endpoint to fetch students from the database
@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")  
        students = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(students=students), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to fetch subjects from the database
@app.route('/subjects', methods=['GET'])
def get_subjects():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM subjects") 
        subjects = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(subjects=subjects), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Database initialization function (optional)
def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Example SQL to create tables if they don't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                program VARCHAR(100)
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INT AUTO_INCREMENT PRIMARY KEY,
                year VARCHAR(20),
                subject_name VARCHAR(100)
            );
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error initializing DB: {e}")

# Call init_db function to ensure tables exist when the app starts
init_db()
