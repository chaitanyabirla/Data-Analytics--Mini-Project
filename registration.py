import pandas as pd
import Data.Dataset as Dataset
from numpy import NaN

def Guide_registration(userid):
    flag = False
    database = pd.read_csv("Data/Guide_data.csv")
    database_r = pd.read_csv("Data/Guide_data.csv")
    datalist = database.values.tolist()

    for i in range(len(datalist)):
        if datalist[i][0] == userid:
            name = input("Enter your name: ")
            department = input("Enter your department: ")

            datalist[i][2] = name
            datalist[i][3] = department

            flag = True
            break

    if not flag:
        print("Invalid registration number.")
    database = pd.DataFrame(datalist, columns=['User ID', 'Password','Department', 'Name','Announcement'])
    appended_data = pd.merge(database_r, database, on='User ID', how='outer')
    appended_data.to_csv("Data/Guide_data.csv", index=True)
    return database
    

def student_registration(regnum):
    flag = False
    database = pd.read_csv("Data/Student_data.csv")
    database_r = pd.read_csv("Data/Student_data.csv")
    datalist = database.values.tolist()
    for i in range(len(datalist)):
        if datalist[i][0] == regnum:
            name = input("Enter your name: ")
            year = int(input("Enter the year you are studying in: "))
            course = input("Enter your class (For e.g: 2LLB-A): ")
            department = input("Enter your department: ")

            datalist[i][2] = name
            datalist[i][3] = year
            datalist[i][4] = department
            datalist[i][5] = course

            flag = True
            break

    if not flag:
        print("Invalid registration number.")
    database = pd.DataFrame(datalist, columns=['User ID', 'Password','Name','Year','Department', 'Course'])
    appended_data = pd.merge(database_r, database, on='User ID', how='outer')
    appended_data.to_csv("Data/Student_data.csv", index=True)
    return database

def internship(regnum):
    intern_detail_list=[]
    for i in range(2211200,2211700):
        j=[i,NaN,NaN,NaN,NaN,NaN,NaN]
        intern_detail_list.append(j)
    
    flag=False
    for i in range(len(intern_detail_list)):
        if intern_detail_list[i][0] == regnum:
            company = input("Enter the company name: ")
            domain = input("Enter the domain of the internship: ")
            weeks = int(input("Enter the number of weeks of work: "))
            guide_name = input("Enter the guide's name: ")
            guide_email = input("Enter the guide's email ID: ")
            guide_designation = input("Enter the guide's designation:")
            
            intern_detail_list[i][1]=company
            intern_detail_list[i][2]=domain
            intern_detail_list[i][3]=weeks
            intern_detail_list[i][4]=guide_name
            intern_detail_list[i][5]=guide_email
            intern_detail_list[i][6]=guide_designation
            flag=True
            break
    if not flag:
        print("Invalid registration number.")
    
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
            course_name = input("Enter the course name: ")
            domain = input("Enter the domain of the course: ")
            start = input("Enter start date in YYYY-MM-DD format: ")
            start_date=datetime.strptime(start, "%Y-%m-%d")
            end = input("Enter end date in YYYY-MM-DD format: ")
            end_date=datetime.strptime(end, "%Y-%m-%d")
            guide_email = input("Enter the guide's email ID: ")
            guide_designation = input("Enter the guide's designation:")
            
            course_detail_list[i][1]=course_name
            course_detail_list[i][2]=domain
            course_detail_list[i][3]=start_date
            course_detail_list[i][4]=end_date
            course_detail_list[i][5]=guide_email
            course_detail_list[i][6]=guide_designation
            flag=True
            break
    if not flag:
        print("Invalid registration number.")
    course_data= pd.DataFrame(course_detail_list, columns=['User ID',"Course Name" , "Domain" , "Start Date" , "End Date" , "Guide Email" , "Guide Designation"])
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
            university = input("Enter the university you are doing reserch under: ")
            domain = input("Enter the domain of the reserch: ")
            start = input("Enter start date in YYYY-MM-DD format: ")
            start_date=datetime.strptime(start, "%Y-%m-%d")
            end = input("Enter end date in YYYY-MM-DD format: ")
            end_date=datetime.strptime(end, "%Y-%m-%d")
            guide_email = input("Enter the guide's email ID: ")
            guide_designation = input("Enter the guide's designation:")
            publication=input("Enter the name of publication your reserch is getting published under:")
            
            reserch_detail_list[i][1]=university
            reserch_detail_list[i][2]=domain
            reserch_detail_list[i][3]=start_date
            reserch_detail_list[i][4]=end_date
            reserch_detail_list[i][5]=guide_email
            reserch_detail_list[i][6]=guide_designation
            reserch_detail_list[i][7]=publication
            flag=True
            break
    if not flag:
        print("Invalid registration number.")
    reserch_data= pd.DataFrame(reserch_detail_list, columns=['User ID',"University Name" , "Domain" , "Start Date" , "End Date" , "Guide Email" , "Guide Designation","Publication"])
    return reserch_data

def stu_intern(user,database):
    intern_data = internship(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Intern_data.csv", index=True)

def stu_course(user,database):
    intern_data = coursework(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Course_data.csv", index=True)

def stu_reserch(user,database):
    intern_data = Reserchwork(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Reserch_data.csv", index=True)
