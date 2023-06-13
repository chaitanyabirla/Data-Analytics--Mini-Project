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

import pandas as pd
import Dataset

def student_registration():
    name = input("Enter your name: ")
    course_name = input("Enter the course name: ")
    year = int(input("Enter the year you are studying in: "))
    course = input("Enter your class\n(For e.g: 2LLB-A): ")
    department=input("Enter your department: ")
    database=Dataset.generate_student_id_modified()

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

    database=Dataset.generate_admin_data()
    database.loc[:, 'Name'] = name
    database.loc[:, 'Course Name'] = department

    admin_data=database.valulijaes.tolist()

    return database,admin_data

print(Admin_registration())
    





    