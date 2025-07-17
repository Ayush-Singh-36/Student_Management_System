# Student_Management_System
A python project that can store student details with the help of mysql
📌 Overview
The Student Management System is a Python-based desktop application that allows you to manage student records efficiently.
It uses Tkinter for the GUI and MySQL for data storage, performing all basic CRUD operations (Create, Read, Update, Delete).

✅ Features
Add Student: Insert new student records.

View Students: Display all stored records.

Update Student: Modify existing student details.

Delete Student: Remove a student record from the database.

🛠 Tech Stack
Python (Tkinter for GUI)

MySQL (Data Storage)

mysql-connector-python (for Python-MySQL integration)

🚀 How to Run the Project
1. Install Required Libraries
pip install mysql-connector-python

2. Create Database and Table in MySQL
Run these queries in MySQL Workbench before starting the app:
CREATE DATABASE college;
USE college;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
);

3. Update Database Connection (if required)
Make sure to edit these details in the code if your credentials are different:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="college"
)

4. Run the Python Script
python student_management_system.py
