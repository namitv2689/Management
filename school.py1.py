import mysql.connector
from mysql.connector import IntegrityError

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password"
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS school")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="school"
)

cursor = mydb.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS student (
        sname VARCHAR (50),
  	admno INT PRIMARY KEY,
  	dob DATE,
  	cls VARCHAR (10),
  	city VARCHAR (30)
)
""")

cursor = mydb.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS teacher (
      tid INT PRIMARY KEY,
      name VARCHAR (50),
      salary INT,
      address VARCHAR (100),
      phone BIGINT
)
""")




cursor = mydb.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS feestructure (
  class VARCHAR(10),
  monthly_fee INT,
  bus_fee INT,
  science_fee INT,
  tech_fee INT,
  total INT
)
""")

cursor = mydb.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS lib_rary (
  book_id INT PRIMARY KEY,
  title VARCHAR(100),
  author VARCHAR(50),
  publisher VARCHAR(50),
  genre VARCHAR(30)
)
""")


cursor = mydb.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS student_attendance (
        admno INT,
  	cls VARCHAR (10),
  	no_of_days_present INT,
  	total_attendance_days INT,
  	percent_attendance FLOAT
)
""")

cursor = mydb.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS student_achievement (
        admno INT,
        sname VARCHAR(50),
  	cls VARCHAR (10),
  	award_name VARCHAR(20),
  	award_date DATE
)
""")



mydb.commit()


def add_student():
    n = input("Student name: ")
    r = input("Roll no.: ")
    d = input("Date of Birth (yyyy-mm-dd): ")
    c = input("Class: ")
    p = input("City: ")
    data = (n, r, d, c, p)
    try: 
        sql = 'insert into student values (%s,%s,%s,%s,%s)'
        cur = mydb.cursor()
        cur.execute(sql, data)
        mydb.commit()
        print("Student record added successfully.\n")
    except IntegrityError as err:
        if err.errno == 1062:
            print (" Duplicate entry. Try again with different Roll no.\n")
        else:
            print ("Database error.\n")         


def show_students():
    print ("List of students in school : \n")
    sql = 'select * from student'
    cur = mydb.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print("Name:", i[0], "Roll No,:", i[1], "Date of Birth:", i[2], "Class:", i[3], "City :", i[4])


def del_student():
    c = input("Class: ")
    r = input("Roll no.: ")
    data = (c, r)
    sql = 'delete from student where cls=%s and admno=%s'
    cur = mydb.cursor()
    cur.execute(sql, data)
    mydb.commit()
    print("Student record deleted successfully.\n")

def add_std_attendance():
    r = input("Roll no.: ")
    c = input("Class: ")
    p = int(input("No. of days student attended school: "))
    t = int(input("No. of working days in school for the academic year: "))
    attendance_percent = float(p/t)
    data = (r,c,p,t,attendance_percent)
    sql = 'insert into student_attendance values (%s,%s,%s,%s,%s)'
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
    print("Student attendance added successfully.\n")


def show_attendance():
    print ("Student Attendance list \n")
    sql = 'select * from student_attendance'
    cur = mydb.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print("Roll No.: ",i[0], "Class: ",i[1],"No. of days student attended school: ",i[2],"No. of working days in school for the academic year: ",i[3],"Attendance percent: ",i[4]*100,"%")


def add_std_achievement():
    r = input("Roll no.: ")
    n = input("Student name: ")
    c = input("Class: ")
    a = input("Award Name: ")
    d = input("Award date (yyyy-mm-dd): ")
    data = (r,n,c,a,d)
    sql = 'insert into student_achievement values (%s,%s,%s,%s,%s)'
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
    print("Student achievement added successfully.\n")

def show_std_achievements():
    print ("Student Acheivements List")
    sql = 'select * from student_achievement'
    cur = mydb.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print("Roll no.: ",i[0],"Student name: ",i[1],"Class: ",i[2],"Award Name: ",i[3],"Award Date: ",i[4])
    


def add_teacher():
    tid = int(input("Teacher ID: "))
    n = input("Name: ")
    s = int(input("Salary: "))
    a = input("Address: ")
    p = int(input("Phone no.: "))
    data = (tid, n, s, a, p)
    try: 
        sql = 'insert into teacher values (%s,%s,%s,%s,%s)'
        cur = mydb.cursor()
        cur.execute(sql, data)
        mydb.commit()
        print("Teacher added successfully.\n")
    except IntegrityError as err:
        if err.errno == 1062:
            print (" Duplicate entry. Try again with different Teacher Id.\n")
        else:
            print ("Database error.\n")


def show_teachers():
    print ("List of teachers in school.\n")
    sql = 'select * from teacher'
    cur = mydb.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print("ID:", i[0], "Name:", i[1], "Salary:", i[2], "Address:", i[3], "Phone:", i[4])


def fee_structure():
    c = input("Class: ")
    m = int(input("Monthly Fee: "))
    b = int(input("Bus Fee: "))
    sc = int(input("Science Fee: "))
    t = int(input("Tech Fee: "))
    total = m + b + sc + t
    data = (c, m, b, sc, t, total)
    sql = 'insert into feestructure values (%s,%s,%s,%s,%s,%s)'
    cur = mydb.cursor()
    cur.execute(sql, data)
    mydb.commit()
    print("Fee Structure Updated Successfully.\n")

def show_fees():
    sql = 'select * from feestructure'
    cur = mydb.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print("Class:", i[0], "Total Fee:", i[5])


def add_book():
    bid = int(input("Book ID: "))
    t = input("Title: ")
    a = input("Author: ")
    p = input("Publisher: ")
    g = input("Genre: ")
    try:
        sql = 'insert into lib_rary values (%s,%s,%s,%s,%s)'
        cur = mydb.cursor()
        cur.execute(sql, (bid, t, a, p, g))
        mydb.commit()
        print("Book Added Successfully.\n")
    except IntegrityError as err:
        if err.errno == 1062:
            print (" Duplicate entry. Try again with different Book Id.\n ")
        else:
            print ("Database error.\n ")
    

def show_books():
    print ("List of books in school library.\n")
    sql = 'select * from lib_rary'
    cur = mydb.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print("Book ID:", i[0], "Title:", i[1], "Author:", i[2], "Publisher:", i[3], "Genre:", i[4])



def menu():
    while True:
        print("""\n******** School Management System ********
        1. Add Student Details
        2. Remove Student Details
        3. Add Sudent Attendance
        4. Add Student Achievements
        5. Teacher Management
        6. Fee Structure
        7. Library
        8. Exit""")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            add_student()
            show_students()
        elif ch == 2:
            del_student()
            show_students()
        elif ch == 3:
            add_std_attendance()
            show_attendance()
        elif ch == 4:
            add_std_achievement()
            show_std_achievements()
        elif ch == 5:
            add_teacher()
            show_teachers()
        elif ch == 6:
            fee_structure()
            show_fees()
        elif ch == 7:
            add_book()
            show_books()
        elif ch == 8:
            break
        else:
            print("Invalid choice! Try again.\n")

menu()


cursor = mydb.cursor()

cursor.execute(""" DROP DATABASE school""")


mydb.close()
