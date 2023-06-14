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


    