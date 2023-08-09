import sqlite3

conn = sqlite3.connect('my_database3.db')

c = conn.cursor()

#Simple way to produce the names of all students in the students table
c.execute('''
        SELECT students.name
        FROM students''')

#Get the names of all students to print
students_list = c.fetchall()

#Print all students' names on the table
print("Currently enrolled students:")
for student in students_list:
    print(student[0])

#Store the chosen student in a variable
student_name = input("Please enter one of the above students' names:\n> ")

#Ensure the entered name was valid
while student_name not in students_list:
    student_name = input("Name not among those listed. Did you spell the name correctly? Try again:\n> ")

#Move our cursor to the courses in the course list
c.execute('''
    SELECT courses.name
    FROM courses
    JOIN student_courses ON courses.id = student_courses.course_id
    JOIN students ON students.id = student_courses.student_id
    WHERE students.name = ?
''', (student_name,))

#Store the student's enrolled courses
courses = c.fetchall() #<= This should look familiar.
print(f"{student_name} is taking the following courses:")
for course in courses: #<= Good, old-fashioned Python loop
    print(course[0])

# Close the connection
conn.close()

