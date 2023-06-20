import pandas as pd  # Import pandas library

#a function to view the student dataset
def view_dataset():
    # Read student data from csv file
    student_data = pd.read_csv("Data/Student_data.csv")
    return student_data# Return the dataframe


# function to view specific student records
def view_student_records():
    student_data = pd.read_csv("Data/Student_data.csv")
    # Get user input for registration numbers
    stud = input("Enter the Registration Numbers of student(s) you want to see details of: ").split()
    # Convert input to integers
    stud = [int(reg) for reg in stud]
    return student_data[student_data['User ID'].isin(stud)] # Return the dataframe with matching records

# function to view the type of students (internship, research, or coursework)
def view_type():
    student_data = pd.read_csv("Data/Student_data.csv")
    # Return the frequency of each type
    return student_data['Type'].value_counts().sort_values(ascending=False)


 # function to view the most popular course among students
def popular_course():
    student_data = pd.read_csv("Data/Student_data.csv")
    if 'Course Work' in student_data.columns:
        # Check if course work column exists
        return student_data['Course Name'].value_counts().sort_values(ascending=False)
    
# function to view the most popular domain among students
def popular_domain():
    student_data = pd.read_csv("Data/Student_data.csv")
    internship_pop_domain = None# Initialize internship popular domain variable
    research_pop_domain = None # Initialize research popular domain variable
    if 'Internship' in student_data.columns:# Check if internship column exists
         
        internship_pop_domain = student_data['Domain'].value_counts().sort_values(ascending=False)
    if 'Research' in student_data.columns:
        research_pop_domain = student_data['Domain'].value_counts().sort_values(ascending=False)
        # Return the frequency of each domain for research and internship students
    return internship_pop_domain, research_pop_domain


# a function to view which students have submitted their reports
def students_submitted():
    student_data = pd.read_csv("Data/Student_data.csv")
    report_status = input("Enter the report names you want to see the status of: ").split()
    week = input("Enter the week: ")
    report_statu = []
    for i in report_status:
         # Convert input to integers and append to list
        report_statu.append(int(i))
    result = []
    for i in report_statu: 
        # Append the report status for each report name and week number to result list
        result.append(student_data[student_data["User ID"] == i, "Week "+week+" Report"])
    return result


# a function to make an announcement for students
def announce(user):
    announcement = input("Please enter your announcement: ")
    guide_data = pd.read_csv("Data/Guide_data.csv")
    # Update the announcement column with the message for the user ID
    guide_data.loc[guide_data['User ID'] == user, 'Announcement'] = announcement
    print()
    print('*'*50)
    print(f"{'Announcement Added!' : ^50}")
    print('*'*50)
    print()
    # Save the updated guide data to csv file
    guide_data.to_csv("Data/Guide_data.csv",index = False)
    return True