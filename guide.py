import Dataset

def view_dataset():
    dataset,_ = Dataset.generate_student_id()
    return dataset

def view_student_records():
    dataset,_ = Dataset.generate_student_id()
    stud = input("Enter the Registration Numbers of student(s) you want to see details of: ").split()
    for i in stud:
        stud[stud.index(i)] = int(i)
    return dataset[dataset['User ID'].isin([stud])]

def view_type():
    dataset,_ = Dataset.generate_student_id()
    return dataset['Type'].value_counts().sort_values(ascending=False)                #check the column name 


def popular_course():
    dataset,_ = Dataset.generate_student_id()
    if dataset['Course Work'] == True:
        return dataset['Course Name'].value_counts().sort_values(ascending=False)     #check the column name 

def popular_domain():
    dataset,_ = Dataset.generate_student_id()
    if dataset['Internship'] == True:
        internship_pop_domain = dataset['Domain'].value_counts().sort_values(ascending=False)             #check the column name 
    if dataset['Reseach'] == True:
        research_pop_domain = dataset['Domain'].value_counts().sort_values(ascending=False)             #check the column name
    return internship_pop_domain, research_pop_domain

def students_submitted():
    dataset,_ = Dataset.generate_student_id()
    report_status = input("Enter the report names you want to see status of: ").split()
    for i in report_status:
        return dataset[i]

def announce():
    announcement = input("Please enter your announcement: ")
    return True, announcement




'''
teahcers can give marks
'''