import pandas as pd

def view_dataset():
    student_data = pd.read_csv("Data/Student_data.csv")
    return student_data

def view_student_records():
    student_data = pd.read_csv("Data/Student_data.csv")
    stud = input("Enter the Registration Numbers of student(s) you want to see details of: ").split()
    stud = [int(reg) for reg in stud]
    return student_data[student_data['User ID'].isin(stud)]

def view_type():
    student_data = pd.read_csv("Data/Student_data.csv")
    return student_data['Type'].value_counts().sort_values(ascending=False)

def popular_course():
    student_data = pd.read_csv("Data/Student_data.csv")
    if 'Course Work' in student_data.columns:
        return student_data['Course Name'].value_counts().sort_values(ascending=False)

def popular_domain():
    student_data = pd.read_csv("Data/Student_data.csv")
    internship_pop_domain = None
    research_pop_domain = None
    if 'Internship' in student_data.columns:
        internship_pop_domain = student_data['Domain'].value_counts().sort_values(ascending=False)
    if 'Research' in student_data.columns:
        research_pop_domain = student_data['Domain'].value_counts().sort_values(ascending=False)
    return internship_pop_domain, research_pop_domain

def students_submitted():
    student_data = pd.read_csv("Data/Student_data.csv")
    report_status = input("Enter the report names you want to see the status of: ").split()
    week = input("Enter the week: ")
    report_statu = []
    for i in report_status:
        report_statu.append(int(i))
    result = []
    for i in report_statu: 
        result.append(student_data[student_data["User ID"] == i, "Week "+week+" Report"])
    return result

def announce(user):
    announcement = input("Please enter your announcement: ")
    guide_data = pd.read_csv("Data/Guide_data.csv")
    guide_data.loc[guide_data['User ID'] == user, 'Announcement'] = announcement
    print()
    print('*'*50)
    print(f"{'Announcement Added!' : ^50}")
    print('*'*50)
    print()
    guide_data.to_csv("Data/Guide_data.csv",index = False)
    return True