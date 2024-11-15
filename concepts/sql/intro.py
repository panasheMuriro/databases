# Objectives:
# Understand the basics of SQL and relational databases.
# Learn how to set up an SQLite database.
# Write your first SQL commands.
# Connect to a database using Python.

# A relational database stores data in tables (relations), where each table has rows (records) and columns (fields).
# Relational databases use primary keys to uniquely identify rows and foreign keys to link tables.

import sqlite3

connection = sqlite3.connect("database_1.db")
cursor = connection.cursor()
print("Databases has been connected successfully")

create_table_command = '''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
'''
cursor.execute(create_table_command)


# inserting data

students = [
    ("Alice", 20, 'A'),
    ("Bob", 22, 'B'),
    ("Charlie", 21, 'C'),
    ("Diana", 19, 'A'),
    ("Ethan", 23, 'B'),
    ("Fiona", 20, 'A'),
    ("George", 24, 'C'),
    ("Hannah", 22, 'B'),
    ("Ian", 21, 'C'),
    ("Jasmine", 20, 'A'),
    ("Kevin", 25, 'B'),
    ("Laura", 18, 'A'),
    ("Michael", 22, 'C'),
    ("Nina", 20, 'A'),
    ("Oscar", 23, 'B'),
    ("Paula", 19, 'A'),
    ("Quinn", 24, 'C'),
    ("Rachel", 21, 'B'),
    ("Steven", 22, 'A'),
    ("Tina", 20, 'B'),
    ("Uma", 19, 'A'),
    ("Victor", 23, 'C'),
    ("Wendy", 22, 'B'),
    ("Xander", 21, 'A'),
    ("Yasmin", 20, 'B')
]


insert_command = "INSERT INTO students (name,age,grade) VALUES (?,?,?);"
cursor.executemany(insert_command, students)

connection.commit()
print("Data inserted successfully")


# retrieving data

retrieve_command = "SELECT * FROM students;"
cursor.execute(retrieve_command)
retrieved_students = cursor.fetchall()

# for student in students:
#     print(student)

# filtering
filtering_command = "SELECT * FROM students WHERE grade = 'A';"
cursor.execute(filtering_command)
filtered_students = cursor.fetchall()

# for student in filtered_students:
#     print(student)
    

#  order
order_command = "SELECT * FROM students ORDER BY age ASC;"
# order_command = "SELECT * FROM students ORDER BY age DESC;"

cursor.execute(order_command)
ordered_students = cursor.fetchall()
# print(ordered_students)

# limiting
limit_command = "SELECT * FROM students LIMIT 5;"
cursor.execute(limit_command)
lim_students = cursor.fetchall()

print(lim_students)

#  unique values with Distinct
dist_command = "SELECT DISTINCT grade FROM students;"
cursor.execute(dist_command)
dist_grades = cursor.fetchall()
# print(dist_grades)

# Aggregate functions
cursor.execute("SELECT COUNT(*) FROM students;")

total_students = cursor.fetchone()[0]

cursor.execute("SELECT AVG(age) FROM students;")
average_age = cursor.fetchone()[0]

cursor.execute("SELECT MAX(grade) FROM students;")
highest_grade = cursor.fetchone()[0]

cursor.execute("SELECT MIN(age) FROM students;")
youngest_age = cursor.fetchone()[0]

# Print results
print(f"Total Students: {total_students}")
print(f"Average Age: {average_age}")
print(f"Highest Grade: {highest_grade}")
print(f"Youngest Age: {youngest_age}")

connection.close()
