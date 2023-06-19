import pandas as pd
import Data.Dataset as Dataset
from numpy import NaN
import pandas as pd

def guide_registration(userid):
    flag = False
    database = pd.read_csv("Data/Guide_data.csv")
    datalist = database.values.tolist()

    for i in range(len(datalist)):
        if datalist[i][0] == userid:
            name = input("Enter our Name: ")
            department = input("Enter your Department: ")
            datalist[i][2] = name
            datalist[i][3] = department
            flag = True
            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()
            break

    if not flag:
        print("Invalid registration number!")

    database = pd.DataFrame(datalist, columns=['User ID', 'Password', 'Name', 'Department', 'Announcement'])
    database.to_csv("Data/Guide_data.csv", index=False)
    return database

def student_registration(regnum):
    flag = False
    database = pd.read_csv("Data/Student_data.csv")
    datalist = database.values.tolist()

    for i in range(len(datalist)):
        if datalist[i][0] == regnum:
            name = input("Enter Your Name: ")
            year = int(input("Enter the Year you are Studying in: "))
            course = input("Enter Your Course: ")
            department = input("Enter Your Department: ")
            datalist[i][2] = name
            datalist[i][3] = year
            datalist[i][4] = department
            datalist[i][5] = course
            flag = True
            break

    if not flag:
        print("Invalid registration number!")

    database = pd.DataFrame(datalist, columns=['User ID', 'Password', 'Name', 'Year', 'Department', 'Course'])
    database.to_csv("Data/Student_data.csv", index=False)
    return database

def internship(regnum):
    intern_detail_list=[]
    for i in range(2211200,2211700):
        j=[i,NaN,NaN,NaN,NaN,NaN,NaN]
        intern_detail_list.append(j)
    
    flag=False
    for i in range(len(intern_detail_list)):
        if intern_detail_list[i][0] == regnum:
            company = input("Enter the Company Name: ")
            domain = input("Enter the Domain in which you are doing your Internship: ")
            weeks = int(input("Enter the Number of Weeks of Internship: "))
            guide_name = input("Enter your Company Guide's Name: ")
            guide_email = input("Enter your Guide's Email ID: ")
            guide_designation = input("Enter your Guide's Designation: ")
            
            intern_detail_list[i][1]=company
            intern_detail_list[i][2]=domain
            intern_detail_list[i][3]=weeks
            intern_detail_list[i][4]=guide_name
            intern_detail_list[i][5]=guide_email
            intern_detail_list[i][6]=guide_designation
            flag=True

            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()

            break
    if not flag:
        print("Invalid registration number!")
    
    intern_data= pd.DataFrame(intern_detail_list, columns=['User ID',"Company Name" , "Domain" , "Weeks of Work" , "Guide Name" , "Guide Email" , "Guide Designation"])
    return intern_data

def coursework(regnum):
    from datetime import datetime
    course_detail_list=[]
    for i in range(2211200,2211700):
        j=[int(i),NaN,NaN,NaN,NaN,NaN,NaN]
        course_detail_list.append(j)
    
    flag=False
    for i in range(len(course_detail_list)):
        if course_detail_list[i][0] == regnum:
            course_name = input("Enter the Course Name: ")
            domain = input("Enter the Domain of your Course: ")
            start = input("Enter Start Date (YYYY-MM-DD): ")
            start_date=datetime.strptime(start, "%Y-%m-%d")
            end = input("Enter End Date (YYYY-MM-DD): ")
            end_date=datetime.strptime(end, "%Y-%m-%d")
            instructor_email = input("Enter your Course Instructor's Email ID: ")
            instructor_designation = input("Enter your instructor's Designation: ")
            
            course_detail_list[i][1] = course_name
            course_detail_list[i][2] = domain
            course_detail_list[i][3] = start_date
            course_detail_list[i][4] = end_date
            course_detail_list[i][5] = instructor_email
            course_detail_list[i][6] = instructor_designation
            flag=True

            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()

            break
    if not flag:
        print("Invalid registration number!")
    course_data= pd.DataFrame(course_detail_list, columns=['User ID',"Course Name" , "Domain" , "Start Date" , "End Date" , "Instructor Email" , "Instructor Designation"])
    return course_data

def Reserchwork(regnum):
    from datetime import datetime
    reserch_detail_list=[]
    for i in range(2211200,2211700):
        j=[int(i),NaN,NaN,NaN,NaN,NaN,NaN,NaN]
        reserch_detail_list.append(j)
    
    flag=False
    for i in range(len(reserch_detail_list)):
        if reserch_detail_list[i][0] == regnum:
            university = input("Enter the University in which you are doing Research: ")
            domain = input("Enter the Domain of your Reserch: ")
            start = input("Enter Start Date (YYYY-MM-DD): ")
            start_date=datetime.strptime(start, "%Y-%m-%d")
            end = input("Enter End Date (YYYY-MM-DD): ")
            end_date=datetime.strptime(end, "%Y-%m-%d")
            guide_email = input("Enter your University Guide's Email ID: ")
            guide_designation = input("Enter ypur Guide's designation: ")
            publication=input("Enter the Name of Publication in which your Reserch is getting Published: ")
            
            reserch_detail_list[i][1]=university
            reserch_detail_list[i][2]=domain
            reserch_detail_list[i][3]=start_date
            reserch_detail_list[i][4]=end_date
            reserch_detail_list[i][5]=guide_email
            reserch_detail_list[i][6]=guide_designation
            reserch_detail_list[i][7]=publication
            flag=True
            
            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()

            break
    if not flag:
        print("Invalid registration number.")
    reserch_data= pd.DataFrame(reserch_detail_list, columns=['User ID',"University Name" , "Domain" , "Start Date" , "End Date" , "Guide Email" , "Guide Designation","Publication"])
    return reserch_data

def stu_intern(user,database):
    intern_data = internship(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Intern_data.csv", index=False)

def stu_course(user,database):
    intern_data = coursework(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Course_data.csv", index=False)

def stu_reserch(user,database):
    intern_data = Reserchwork(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Reserch_data.csv", index=False)