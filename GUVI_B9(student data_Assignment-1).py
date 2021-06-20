import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="aswin")
cur = con.cursor()

# Function_To_Call_add_student........
def add_student():
    Name= str(input("Enter Student Name: "))
    Department = str(input("Enter Student Department: "))
    College	 = str(input("Enter Student College name: "))
    Mark_1= int(input("Enter Student Mark 1: "))
    Mark_2= int(input("Enter Student Mark 2: "))
    Mark_3 = int(input("Enter Student Mark 3: "))
    Mark_4 = int(input("Enter Student Mark 4: "))
    Mark_5 = int(input("Enter Student Mark 5: "))
    Total_Mark = Mark_1 + Mark_2 + Mark_3 + Mark_4 + Mark_5
    Average = round (Total_Mark/5)
    Grade = 'X'
    if (Average >= 0 and Average<30):
        Grade="c"
        print('Grade is C')
    elif(Average>30 and Average<60):
        Grade="B"
        print('Grade is B')
    elif(Average>61 and Average<80):
        Grade="A"
        print('Grade is A')
    elif(Average>=81 and Average<=100):
        Grade="S"
        print('Grade is S')
    else:
        print("Enter the correct Marks")
    query = "insert into sutend_of_college(Name,Department,College,Mark_1,Mark_2,Mark_3,Mark_4,Mark_5,Total_Mark,Average,Grade) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    data = (Name,Department,College,Mark_1,Mark_2,Mark_3,Mark_4,Mark_5,Total_Mark,Average,Grade)
    cur.execute(query,data)
    con.commit()
    print("Operation done")

# Function_To_Call_Cal_garde........
def Cal_grade(Average):
    if (Average >= 0 and Average<30):
        Grade="c"
        print('Grade is C')
    elif(Average>30 and Average<60):
        Grade="B"
        print('Grade is B')
    elif(Average>61 and Average<80):
        Grade="A"
        print('Grade is A')
    elif(Average>=81 and Average<=100):
        Grade="S"
        print('Grade is S')
    else:
        print("Enter the correct Marks")

# Function_To_Get_Student........
def Get_Student():
    I = str(input("Please Enter the Student id: "))
    cur.execute("""select * from sutend_of_college where id = \""""+str(I)+"""\";""")
    result = cur.fetchall()
    for i in result:
        name=i
        print(name)

# Function_Get_all_student........
def Get_all_student():
    cur.execute("select * from sutend_of_college")
    result = cur.fetchall()
    for i in result:
        print(i)

# Function_Delete_student........
def Delete_student():
    Name = str(input("enter the student name: "))
    cur.execute("""DELETE from sutend_of_college WHERE Name= \"""" +Name + """\";""")
    con.commit()
    print("student deleted successfully")

# Function_Update_student........
def update_student():
    name = str(input("enter the name: "))
    cur.execute("""select Name from sutend_of_college where Name =\"""" + name + """\";""")
    name1 = cur.fetchone()
    for i in name1:
        name2 = i

    def change_name():
        new_name = str(input("enter the new name: "))
        cur.execute("""UPDATE 
                           sutend_of_college
                       SET
                           Name = REPLACE(Name,\"""" + name + """\",\"""" + new_name + """\")
                       WHERE
                           Name IS NOT NULL;""")
        con.commit()
        print("changes completed")


    def change_College_name():
        old_name = str(input("enter the old College name: "))
        new_name = str(input("enter the new College name: "))
        cur.execute("""UPDATE 
                            sutend_of_college
                       SET
                            College = REPLACE(College,\"""" + old_name + """\",\"""" + new_name + """\")
                       WHERE
                            College IS NOT NULL;""")
        print("changes completed")
        con.commit()

    def change_Department_name():
        old_name = str(input("enter the old Department name: "))
        new_name = str(input("enter the new Department name: "))
        cur.execute("""UPDATE 
                            sutend_of_college
                       SET
                            Department = REPLACE(Department,\"""" + old_name + """\",\"""" + new_name + """\")
                       WHERE
                            Department IS NOT NULL;""")
        print("changes completed")
        con.commit()

    def change_mark(Subject):
        cur.execute("""select """+Subject+""" from sutend_of_college where Name =\"""" + name + """\";""")
        Mark = cur.fetchone()
        for i in Mark:
            Mark = i
        cur.execute("""select Total_Mark from sutend_of_college where Name =\"""" + name + """\";""")
        totalMark = cur.fetchone()
        for i in totalMark:
            totalMark = i
        old_grade = Cal_grade(totalMark/5)
        updated_total = totalMark - Mark
        new_Mark = int(input("enter the new subject mark: "))
        new_total = new_Mark + updated_total
        old_Avg=round( totalMark/5)
        Avg = round(new_total/5)
        new_grade = Cal_grade(Avg)
        cur.execute("""UPDATE
                            sutend_of_college
                       SET
                            """+Subject+""" = REPLACE("""+Subject+""",""" + str(Mark) + """,""" + str(new_Mark) + """),
                            Total_Mark = REPLACE(Total_Mark,""" + str(totalMark) + """,""" + str(new_total) + """),
                            Average = REPLACE(Average,""" + str(old_Avg) + """,""" + str(Avg) + """),
                            Grade = REPLACE(Grade,\"""" + str(old_grade) + """\",\"""" + str(new_grade) + """\")
                       WHERE
                            Name=\""""+name+"""\";""")
        con.commit()
        print("changes completed")

    while (True):

        if name2 != name:
            print("enter the valid name")
            break
        elif name2 == name:
            print("1. Change Name")
            print("2. Change College_NAme")
            print("3. Change Department")
            print("4. Change Mark1")
            print("5. change Mark2")
            print("6. change Mark3")
            print("7. change Mark4")
            print("8. change Mark5")
            print("9. Quit")
            b = int(input("enter the number: "))
            if b == 1:
                change_name()
            elif b == 2:
                change_College_name()
            elif b == 3:
                change_Department_name()
            elif b == 4:
                change_mark("Mark_1")
            elif b == 5:
                change_mark("Mark_2")
            elif b == 6:
                change_mark("Mark_3")
            elif b == 7:
                change_mark("Mark_4")
            elif b == 8:
                change_mark("Mark_5")
            elif b == 9:
                break
        else:
            break




while (True):
    print('Menu')
    print('1. Add Student')
    print('2. Get student')
    print('3. Get all student')
    print('4. Update student')
    print('5. Delete student')
    print('6. Exit')
    a = int(input("Enter the value: "))
    if a == 6:
        break
    elif a == 1:
        add_student()
    elif a ==2:
        Get_Student()
    elif a==3:
        Get_all_student()
    elif a==4:
        update_student()
    elif a==5:
        Delete_student()