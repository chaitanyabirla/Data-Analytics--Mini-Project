import pandas as pd
# a function to create a weekly report for a student
def weekly_report(student_id):
    stud_dataset = pd.read_csv("Data/Student_data.csv")
    week = input("Enter Week Number: ")
    report = input("Enter your Week "+week+" Report: ")
    # to update the student data with the report for that week
    stud_dataset.loc[stud_dataset["User ID"] == student_id, "Week "+week+" Report"]= report   
    stud_dataset.to_csv("Data/Student_data.csv", index=False)
    print('*'*50)
    print(f"{'Report Addess Successfully!' : ^50}")
    print('*'*50)
    print()

#  a function to create a final report for a student
def final_report(student_id):
    stud_dataset = pd.read_csv("Data/Student_data.csv")
    report = input("Enter your Final Report: ")
    # To update the student data with the final report
    stud_dataset.loc[stud_dataset["User ID"] == student_id, "Final Report"]= report
    stud_dataset.to_csv("Data/Student_data.csv", index=False)
    print('*'*50)
    print(f"{'Report Addess Successfully!' : ^50}")
    print('*'*50)
    print()