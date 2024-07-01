import json
import os
import sys

if __name__== "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_dir, "src"))

from src import *
# from src import read_write_json


class Teacher:
    
    def signup_as_teacher():
        """adds new teacher to teacher db
        """
        name = input("Enter name: ").capitalize()
        id = int(input("Enter id: "))

        while repeated_record.isrepeated("Id",id):
            print("The person with this id already exists!")
            id = int(input("Enter id: "))

        subject = input("Enter subject: ")
        address = input("Enter address: ")
        email = input("Enter email: ")

        while not validate_email.check_email(email):
            print("Invalid email!")
            email = input("Enter email: ")

        ph_no = (input("Enter phone no:"))

        while len(ph_no) != 10:
            print("Invalid phone number!")
            ph_no = input("Enter phone no: ")

        list_of_each = []  
        list_of_each = read_write_json.read_from_json_file("data/teacher.json", list_of_each)
        
        dict_teacher_record = {"Name" : name,
                            "Id" : id,
                            "Subject" : subject,
                            "address" : address,
                            "email" : email,
                            "phone no" : ph_no}
        
        list_of_each.append(dict_teacher_record)
    
        read_write_json.write_to_json_file("data/teacher.json", list_of_each)

    def login_as_teacher():
        """if this function returns True
        then teacher will get access to teacher functions
        Returns:
            bool: True if teacher is in teacher db
        """
        name = input("Enter name: ").capitalize()
        id = int(input("Enter Id: "))

        bool_found = False

        teacher_records = []
        teacher_records = read_write_json.read_from_json_file("data/teacher.json", teacher_records)

        for each_teacher_record in teacher_records:

            if each_teacher_record["Name"] == name and each_teacher_record["Id"] == id:
                bool_found = True
                break;

        return bool_found


    def add_student():
        """This function is accessed by teacher 
            only to add new student details
        """
        name = input("Enter name: ").capitalize()
        roll = int(input("Enter roll no: "))

        while repeated_record.isrepeated("roll", roll):
            print("The student with this roll no already exists!")
            roll = int(input("Enter roll no: "))

        email = input("Enter email: ")

        while not  validate_email.check_email(email):
            print("Invalid email!")
            email = input("Enter email: ")

        address = input("Enter address: ")
        ph_no = input("Enter phone no: ")
        
        while len(ph_no) != 10:
            print("Invalid phone number!")
            ph_no = input("Enter phone no: ")
        
        marks = []
        print("Enter marks of maths , c++, python: ")
        for i in range(3):
            mark = int(input())
            marks.append(mark)
        dict1 = {
                "Name" : name,
                "roll" : roll,
                "email" : email,
                "address" : address,
                "phone no" : ph_no,
                "Marks" : marks
                }
        
        all_records = []
        all_records = read_write_json.read_from_json_file("data/student.json", all_records)
        
        all_records.append(dict1)

        read_write_json.write_to_json_file("data/student.json", all_records)

    def display_all():
        """This function displays 
            general detail(name, roll no, email)
            of all the students in student database
            This function can only be accessed by teacher
        """
        all_students = []  
        try:  
            with open("data/student.json", "r")  as file:
                all_students = json.load(file)
        except:
            print("File is empty!")
        else:
            print("===============RECORD OF ALL STUDENTS (GENERAL)==============")
            for each_student in all_students:
                print("Name : " + each_student["Name"])
                print("roll.no : " + str(each_student["roll"]))
                print("email : " + each_student["email"])
                # list_of_each = list(each_student.items())
                # dict_of_each = dict(list_of_each[:3])
                # for key, value in dict_of_each.items():
                #     print(f"{key} : {value}")
                    
                print("---------------------------------------------")

    def search_student():
        """This function can be accessed by both
            teacher and student.
            This function displays 
            details of searched student.
            This function also give options to 
            view calculations(pass_fail_status,percent,rank,highes_lowest scores)
            of searched student
        """
        name = input("Enter name: ").capitalize()
        roll = int(input("Enter roll: "))
        all_records = []
        is_empty = False
        try:
            with open("data/student.json") as file:
                all_records = json.load(file)
        except:
            is_empty = True
            print("Database is empty!")

        Not_found = True
        if not is_empty:
            for each_student in all_records:
                if each_student["Name"] == name and each_student["roll"] == roll:
                    print(f"===========DETAILS OF {name.upper()}==============")
                    for key, value in each_student.items():
                        print(f"{key} : {value}")
                    Not_found = False
                    break;

            if Not_found:
                print("SEARCHED STUDENT NOT FOUND!")
            else:
                x = 8
                while x!=0:
                    x = int(input("""Enter:
0. to exit program
1. to check pass or fail status: 
2. to check percentage: 
3. to check highest and lowest marks: 
4. to check rank
: """))
                    if x == 0:
                        exit
                    elif x == 1:
                        print( calculations.pass_fail_determination(name, roll))
                    elif x == 2:
                        if  calculations.pass_fail_determination(name, roll) == "pass":
                            print( calculations.percentage(name, roll))
                        else:
                            print("No percentage for failed student!")
                    elif x == 3:
                         calculations.highest_and_lowest_scores(name, roll)
                    elif x == 4:
                        if  calculations.pass_fail_determination(name, roll) == "pass":
                             calculations.rank_calculation(name, roll)
                        else:
                            print("No rank for failed student!")
                    else:
                        print("Invalid input! please try again: ")
                        Teacher.search_student()

    def remove_student():
        """Can only be accessed by teacher.
            This funcion will remove details of specific student
        """
        name = input("Enter name: ").capitalize()
        roll = int(input("Enter roll: "))
        all_records = []
        is_empty = False
        try:
            with open("data/student.json", "r") as file:
                all_records = json.load(file)
        except:
            is_empty = True

        NotFound = True
        if is_empty:
            print("File is empty!")

        else:
            for each_student in all_records:
                if each_student["Name"] == name and each_student["roll"] == roll:
                    all_records.remove(each_student)
                    print(f"===========DETAILS OF {name.upper()} IS DELETED==============")
                    NotFound = False
                    break
            if NotFound:
                print("SEARCHED STUDENT NOT FOUND!")

        read_write_json.write_to_json_file("data/student.json", all_records)

    def teacher_functions():
        """All the functions that can be accessed
        by teacher are here
        """
        x=8
        while x!=0:
            x = int(input("Enter: \n0. to exit \n1. to add new student \n2. to display all students\n3. to display specific student \n4. to remove student\n: "))

            if x == 1:
                Teacher.add_student()

            elif x == 2:
                Teacher.display_all()

            elif x == 3:
                Teacher.search_student()
            elif x == 4:
                Teacher.remove_student()

            elif x == 0:
                exit
            
            else:
                print("Invalid Input. Please Try again! ")
                Teacher.teacher_functions()

class Student:

    def login_as_student():
        """This function gives student access to
            student funtions if name and roll of 
            student is found in student db

        Returns:
            bool : true if student is in student db
        """
        name = input("Enter name: ").capitalize()
        roll = int(input("Enter roll.no: "))

        bool_found = False

        student_records = []
        student_records = read_write_json.read_from_json_file("data/student.json", student_records)

        for each_student_record in student_records:

            if each_student_record["Name"] == name and each_student_record["roll"] == roll:
                bool_found = True
                break;

        return bool_found


    def student_functions():
        """All the functions students can perform
            are accessed from here
        """
        x = int(input("""Enter:
0. to exit
1. to view your details
: """))

        if x == 1:
            Teacher.search_student()

        elif x == 0:
            exit
        
        else:
            print("Invalid Input! please try again")
            Student.student_functions()

def initial_function():
    """This function is used to perform initial
    sign ups and logins
    """
    x = int(input("0. exit 1. Teacher 2. Student: "))
    if x == 1:
        y = int(input("0. exit 1. Sign up 2. Log in: "))
        if y == 1:
            print("========ADD YOUR DETAILS TO SIGN UP======")
            Teacher.signup_as_teacher()
            print("=========LOGGING IN AS TEACHER========")
            k=Teacher.login_as_teacher()
            while not k:
                print("Teacher not found in db! please try again")
                k=Teacher.login_as_teacher()
            Teacher.teacher_functions()
        elif y == 2:
            print("=========LOGGING IN AS TEACHER========")
            k=Teacher.login_as_teacher()
            while not k:
                print("Teacher not found in db! please try again")
                k=Teacher.login_as_teacher()
            Teacher.teacher_functions()
        elif y == 0:
            exit
        else:
            print("Invalid input. please try again")
            initial_function()

    elif x == 2:
        print("=========LOGGING IN AS STUDENT========")
        k = Student.login_as_student()
        while not k:
            print("student not found. please try again!")
            k = Student.login_as_student()
        
        Student.student_functions()
        

    elif x == 0:
        exit
    else:
        print("Invalid Input. Please try again")
        initial_function

initial_function()

            
            
                
    
