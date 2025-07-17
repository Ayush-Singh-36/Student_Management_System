import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "college"
)
cursor = conn.cursor()

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    if name and age and grade:
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
        conn.commit()
        messagebox.showinfo("success", "student added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input error", "All fields are required!")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    display_box.delete(1.0, tk.END)
    for row in records:
        display_box.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}\n")

def update_student():
    student_id = id_entry.get()
    new_name = name_entry.get()
    new_age = age_entry.get()
    new_grade = grade_entry.get()

    if student_id and new_name and new_age and new_grade:
        cursor.execute("UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s", (new_name, new_age, new_grade, student_id))
        conn.commit()
        messagebox.showinfo("success", "student updated successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input error", "All fields are required!")
        
def delete_student():
    student_id = id_entry.get()
    if student_id:
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        messagebox.showinfo("success", "student delete successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please enter student ID to delete!")

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

root = tk.Tk()
root.title("student Management System")
root.geometry("400x500")

tk.Label(root, text="student ID (for Update/Delete):").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Grade").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

tk.Button(root, text = "Add Student", command = add_student).pack(pady = 5)
tk.Button(root, text = "View Student", command = view_students).pack(pady = 5)
tk.Button(root, text = "Update Student", command = update_student).pack(pady = 5)
tk.Button(root, text = "Delete Student", command = delete_student).pack(pady = 5)

display_box = tk.Text(root, height=15, width=40)
display_box.pack()

root.mainloop()