import pandas as pd

def enter_report(student_id):
    stud_dataset = pd.read_csv("Data/Student_data.csv")
    #student_id = int(input("Enter your User ID: "))
    week = input("Enter Week Number: ")
    report = input("Enter your Week "+week+" Report: ")
    stud_dataset.loc[stud_dataset["User ID"] == student_id, "Week "+week+" Report"]= report
    stud_dataset.to_csv("Data/Student_data.csv", index=False)
    print('*'*50)
    print(f"{'Report Addess Successfully!' : ^50}")
    print('*'*50)
    print()