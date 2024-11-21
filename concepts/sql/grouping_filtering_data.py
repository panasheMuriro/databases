# Objectives:
# Understand how to group data using GROUP BY.
# Filter grouped data with HAVING.
# Learn about subqueries (nested queries).
# Use Python to implement grouping and filtering.


import sqlite3

connection = sqlite3.connect("database_1.db")
cursor = connection.cursor()


# Query to count students in each grade
cursor.execute("""
SELECT grade, COUNT(*) AS student_count
FROM students
GROUP BY grade;
""")
grouped_data = cursor.fetchall()

# Print results
print("Number of students in each grade:")
for row in grouped_data:
    print(f"Grade: {row[0]}, Count: {row[1]}")


# Query to filter grades with more than 50 students
cursor.execute("""
SELECT grade, COUNT(*) AS student_count
FROM students
GROUP BY grade
HAVING COUNT(*) > 50;
""")
filtered_data = cursor.fetchall()

# Print results
print("Grades with more than 50 students:")
for row in filtered_data:
    print(f"Grade: {row[0]}, Count: {row[1]}")


# Query to find students older than the average age
cursor.execute("""
SELECT name, age
FROM students
WHERE age > (SELECT AVG(age) FROM students);
""")
older_students = cursor.fetchall()

# Print results
print("Students older than the average age:")
for student in older_students:
    print(f"Name: {student[0]}, Age: {student[1]}")


# Close the connection
connection.close()