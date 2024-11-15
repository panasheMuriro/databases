import sqlite3

connection = sqlite3.connect("database_1.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
""")


print("Courses table created successfully.")

courses = [
    ("Mathematics", 1),
    ("Physics", 2),
    ("Chemistry", 3),
    ("Biology", 1),
    ("Computer Science", 2),
    ("History", 3),
    ("Economics", 4),
    ("Art", 5)
]

cursor.executemany("INSERT INTO courses (course_name, student_id) VALUES (?, ?);", courses)

"""
Join Type	Description
INNER JOIN	Returns rows with matching values in both tables.
LEFT JOIN	Returns all rows from the left table and matching rows from the right table.
RIGHT JOIN	Returns all rows from the right table and matching rows from the left table. (Not supported in SQLite.)
FULL OUTER JOIN	Returns all rows when there is a match in either table. (Not supported in SQLite.)
"""

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses ON students.id = courses.student_id;
""")

results = cursor.fetchall()
for row in results:
    print(f"Student: {row[0]}, Course: {row[1]}")

connection.commit()
connection.close()
