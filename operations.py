import sqlite3

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, department) VALUES (?, ?, ?)",
        (name, age, department)
    )

    conn.commit()
    conn.close()

    print("Student added successfully!")

def view_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No students found.")
    
    for student in students:
            print(f"""
            ID: {student[0]}
            Name: {student[1]}
            Age: {student[2]}
            Department: {student[3]}
            ------------------------
            """)
    conn.close()
def search_student():

    name = input("Enter student name: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )

    students = cursor.fetchall()

    if len(students) == 0:
        print("Student not found.")
    else:
        for student in students:
            print(f"""
            ID: {student[0]}
            Name: {student[1]}
            Age: {student[2]}
            Department: {student[3]}
            ------------------------
            """)

    conn.close()
def update_student():
    student_id = int(input("Enter Student ID to update: "))

    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    new_department = input("Enter new department: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, department = ?
        WHERE id = ?
    """, (new_name, new_age, new_department, student_id))

    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student updated successfully!")

    conn.close()
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted successfully!")

    conn.close()
