from numpy import NaN
import pandas as pd

def generate_student_id():
    student_list = []
    for i in range(2211200,2211700):
       j = [i,NaN,NaN,NaN,NaN,NaN,NaN]
       student_list.append(j)
    student_data= pd.DataFrame(student_list, columns=['User ID', 'Password','Name', 'Course Name', 'Year', 'Course',"Department"])
    return student_data, student_list



     if internship_type == "research":
        research_columns = input("Enter the additional research columns separated by commas: ").split(",")
        for column_name in research_columns:
            j.append(NaN)  # Add NaN value for each research column
    elif internship_type == "coursework":
        coursework_columns = input("Enter the additional coursework columns separated by commas: ").split(",")
        for column_name in coursework_columns:
            j.append(NaN)  # Add NaN value for each coursework column

    # Define column names for the DataFrame
    column_names = ['User ID', 'Password', 'Name', 'Course Name', 'Year', 'Course', 'Department']
    column_names.extend(research_columns)  # Add research columns to column names if applicable
    column_names.extend(coursework_columns)  # Add coursework columns to column names if applicable

    student_data = pd.DataFrame(student_list, columns=column_names)
    return student_data, student_list