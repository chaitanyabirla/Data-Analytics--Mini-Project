import pandas as pd
import Dataset

def student_registration(user):
    dataset,_ = Dataset.generate_student_id()
    if dataset.loc[dataset['User ID'] == user, 'Password'].values[0]:
            stud_Pswd = input("Set Password: ")
            if input("Confirm Password: ") == stud_Pswd:
                dataset.loc[dataset['User ID'] == user, 'Password'] = stud_Pswd
                print("Loged In Successfully!")
                status = True

    name = input("Enter your name: ")
    course_name = input("Enter the course name: ")
    year = int(input("Enter the year you are studying in: "))
    course = input("Enter your class\n(For e.g: 2LLB-A): ")
    department=input("Enter your department: ")
    database=dataset.generate_student_data_modified()

    database.loc[:, 'Name'] = name
    database.loc[:, 'Department'] = department
    database.loc[:, 'Course Name'] = course_name
    database.loc[:, 'Year'] = year
    database.loc[:, 'Course'] = course
    student_data = database.values.tolist()



    return student_data,database

#print(student_registration())


def Admin_registration():
    name = input("Enter your name: ")
    department=input("Enter your department: ")

    database=dataset.generate_admin_data()
    database.loc[:, 'Name'] = name
    database.loc[:, 'Course Name'] = department

    admin_data=database.values.tolist()

    return database,admin_data

#print(Admin_registration())

def Guide_registration():
    name = input("Enter your name: ")
    department=input("Enter your department: ")

    database=dataset.generate_guide_data()
    database.loc[:, 'Name'] = name
    database.loc[:, 'Department'] = department

    Guide_data=database.values.tolist()

    return database,Guide_data




    
# print(Guide_registration())


'''import csv
def student_detail(dataset):
    
    name=input("Enter your name:")
    course_name=("Enter the course name:")
    year=int(input("Enter the year you are studying in:"))
    course=input("Enter your class\n(For e.g: 2LLB-A):")
    with open('dataset.csv','r') as ID:
        content=csv.reader(ID)
        with open('new_dataset.csv','w',newline='') as details:
            details=csv.writer(details)
            for i in content:
                i.append(name)
                i.append(course_name)
                i.append(year)
                i.append(course)
                details.writerow(i)

dataset=
student_detail(dataset)'''
from numpy import NaN
import pandas as pd
import Dataset

def student_registration():
    flag = False
    regnum=int(input("enter your registration number"))
    database,datalist=Dataset.generate_student_id()
    for i in range(len(datalist)):
        if datalist[i][0] == regnum:
            name = input("Enter your name: ")
            course_name = input("Enter the course name: ")
            year = int(input("Enter the year you are studying in: "))
            course = input("Enter your class (For e.g: 2LLB-A): ")
            department = input("Enter your department: ")

            # Update the values only in the specific row that matches the registration number
            datalist[i][2] = name
            datalist[i][3] = department
            datalist[i][4] = course_name
            datalist[i][5] = year
            datalist[i][6] = course
            flag = True
            break
    if not flag:
        print("Invalid registration number.")

    database = pd.DataFrame(datalist, columns=['User ID', 'Password','Name', 'Course Name', 'Year', 'Course',"Department"])
    return database,datalist


def Admin_registration():
    name = input("Enter your name: ")
    department=input("Enter your department: ")

    database=Dataset.generate_admin_data()
    database.loc[:, 'Name'] = name
    database.loc[:, 'Course Name'] = department

    admin_data=database.values.tolist()

    return database,admin_data

#print(Admin_registration())

def Guide_registration():
    name = input("Enter your name: ")
    department=input("Enter your department: ")

    database=Dataset.generate_guide_data()
    database.loc[:, 'Name'] = name
    database.loc[:, 'Department'] = department

    Guide_data=database.values.tolist()

    return database,Guide_data
    
# print(Guide_registration())

def internship():
    intern_detail_list=[]
    for i in range(2211200,2211700):
        j=[i,NaN,NaN,NaN,NaN,NaN,NaN]
        intern_detail_list.append(j)
    
    flag=False
    regnum=int(input("enter your registration number"))
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
    intern_data= pd.DataFrame(intern_detail_list, columns=['User ID',"Company" , "Domain" , "Weeks of Work" , "Guide Name" , "Guide Email" , "Guide Designation"])
    return intern_data
print(internship())