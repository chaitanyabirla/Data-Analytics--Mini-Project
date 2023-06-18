import Dataset
def view_dataset():
    student_data,_ = Dataset.generate_student_id()
    return student_data

def view_student_records():
    student_data, _ = Dataset.generate_student_id()
    stud = input("Enter the Registration Numbers of student(s) you want to see details of: ").split()
    stud = [int(reg) for reg in stud]
    return student_data[student_data['User ID'].isin(stud)]

def view_type():
    student_data, _ = Dataset.generate_student_id()
    return student_data['Type'].value_counts().sort_values(ascending=False)

def popular_course():
    student_data, _ = Dataset.generate_student_id()
    if 'Course Work' in student_data.columns:
        return student_data['Course Name'].value_counts().sort_values(ascending=False)

def popular_domain():
    student_data, _ = Dataset.generate_student_id()
    internship_pop_domain = None
    research_pop_domain = None
    if 'Internship' in student_data.columns:
        internship_pop_domain = student_data['Domain'].value_counts().sort_values(ascending=False)
    if 'Research' in student_data.columns:
        research_pop_domain = student_data['Domain'].value_counts().sort_values(ascending=False)
    return internship_pop_domain, research_pop_domain

def students_submitted():
    student_data, _ = Dataset.generate_student_id()
    report_status = input("Enter the report names you want to see the status of: ").split()
    return student_data[report_status]

def announce():
    announcement = input("Please enter your announcement: ")
    return True, announcement



'''
teahcers can give marks
'''