import mysql.connector as sql

# Connect to the database (or create it if it doesn't exist)
db = sql.connect(host='localhost',user='root',passwd='root',database='School',auth_plugin='mysql_native_password')
cursor = db.cursor()
# cursor.execute('CREATE DATABASE School')

# Create tables
cursor.execute('''CREATE TABLE Subjects (subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE Teachers (teacher_id INTEGER PRIMARY KEY,
    teacher_name TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE Classes (class_id INTEGER PRIMARY KEY,
    class_name TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE Timetable (timetable_id INTEGER PRIMARY KEY,
    day_of_week TEXT NOT NULL,period_no INTEGER NOT NULL,class_id INTEGER,
    subject_id INTEGER,teacher_id INTEGER)''')

# Insert data
data1="INSERT INTO Subjects VALUES (%s,%s)"
data2="INSERT INTO Teachers VALUES (%s,%s)"
data3="INSERT INTO Classes VALUES (%s,%s)"
val1=[(1, 'Math'), (2, 'Physics'), (3, 'Chemistry'), (4, 'Computer'), (5, 'English'),]
val2=[(1, 'Mr. Smith'), (2, 'Ms. Johnson'), (3, 'Dr. Brown'), (4, 'Mrs. Davis'), (5, 'Mr. Wilson'),]
val3=[(1, '12A'), (2, '12B'), (3, '12C'),(4,'12D'),(5,'12E'),]
db.commit()
cursor.executemany(data1,val1)
cursor.executemany(data2,val2)
cursor.executemany(data3,val3)
print('Data inserted successfully')

# Display Records inserted
cursor.execute('select *from Subjects')
myresult=cursor.fetchall()
print('Subject Table-')
for i in myresult:
    print(i)

cursor.execute('select *from Teachers')
myresult=cursor.fetchall()
print('Teachers Table-')
for i in myresult:
    print(i)

cursor.execute('select *from Classes')
myresult=cursor.fetchall()
print('Classes Table-')
for i in myresult:
    print(i)

# Update timetable
cursor.execute("INSERT INTO Timetable VALUES ({}, '{}', {}, {}, {}, {})".format(1, 'Monday', 1, 1, 1, 1))
cursor.execute("INSERT INTO Timetable VALUES ({}, '{}', {}, {}, {}, {})".format(2, 'Tuesday', 2, 2, 2, 2))
cursor.execute("INSERT INTO Timetable VALUES ({}, '{}', {}, {}, {}, {})".format(3, 'Wednesday', 3, 3, 3, 3))
cursor.execute("INSERT INTO Timetable VALUES ({}, '{}', {}, {}, {}, {})".format(4, 'Thursday', 4, 4, 4, 4))
cursor.execute("INSERT INTO Timetable VALUES ({}, '{}', {}, {}, {}, {})".format(5, 'Friday', 5, 5, 5, 5))

# Display timetable
cursor.execute('''SELECT Timetable.timetable_id, Timetable.day_of_week, Timetable.period_no, Classes.class_name, Subjects.subject_name, Teachers.teacher_name 
               FROM Timetable 
               JOIN Classes ON Timetable.class_id = Classes.class_id
               JOIN Subjects ON Timetable.subject_id = Subjects.subject_id
               JOIN Teachers ON Timetable.teacher_id = Teachers.teacher_id''')

timetable_data = cursor.fetchall()
print("Timetable:")
for row in timetable_data:
    print(row)

# Alter timetable (change a record)
cursor.execute("UPDATE Timetable SET teacher_id = {} WHERE timetable_id = {}".format(2, 1))

# Display updated timetable
cursor.execute('''SELECT Timetable.timetable_id, Timetable.day_of_week, Timetable.period_no, Classes.class_name, Subjects.subject_name, Teachers.teacher_name
FROM Timetable
JOIN Classes ON Timetable.class_id = Classes.class_id
JOIN Subjects ON Timetable.subject_id = Subjects.subject_id
JOIN Teachers ON Timetable.teacher_id = Teachers.teacher_id''')

timetable_data = cursor.fetchall()
print("\nUpdated Timetable:")
for row in timetable_data:
    print(row)

# Delete record from timetable
cursor.execute("DELETE FROM Timetable WHERE timetable_id = {}".format(5))

# Commit the changes and close the connection
db.commit()
db.close()
