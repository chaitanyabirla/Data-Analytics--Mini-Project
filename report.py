import pandas as pd

def weekly_report(student_id):
    stud_dataset = pd.read_csv("Data/Student_data.csv")
    week = input("Enter Week Number: ")
    report = input("Enter your Week "+week+" Report: ")
    stud_dataset.loc[stud_dataset["User ID"] == student_id, "Week "+week+" Report"]= report
    stud_dataset.to_csv("Data/Student_data.csv", index=False)
    print('*'*50)
    print(f"{'Report Addess Successfully!' : ^50}")
    print('*'*50)
    print()

def final_report(student_id):
    stud_dataset = pd.read_csv("Data/Student_data.csv")
    report = input("Enter your Final Report: ")
    stud_dataset.loc[stud_dataset["User ID"] == student_id, "Final Report"]= report
    stud_dataset.to_csv("Data/Student_data.csv", index=False)
    print('*'*50)
    print(f"{'Report Addess Successfully!' : ^50}")
    print('*'*50)
    print()