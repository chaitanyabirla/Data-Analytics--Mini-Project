import csv
import os.path
import pandas as pd

def enter_report():
    stud_dataset = pd.read_csv("Data/Student_data.csv")
    student_id = int(input("Enter your User ID: "))
    week = input("Enter Week Number: ")
    report = input("Enter your Week "+week+" Report: ")
    stud_dataset.loc[stud_dataset["User ID"] == student_id, "Week "+week+" Report"]= report
    stud_dataset.to_csv("Data/Student_data.csv", index=False)
    print("Report Addess Successfully!")


print("Welcome to the Weekly Report System")

while True:
    print("\nMenu:")
    print("1. Enter Report")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        enter_report()
    
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Weekly Report System!")






# import pandas as pd
# import os.path

# def append_csv_files(file1, file2, output_file):
#     # Check if the output file exists, if not, create it and write the header
#     if not os.path.isfile(output_file):
#         with open(output_file, "w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(["User ID", "Password", "Name", "Course Name", "Year", "Course", "Department", "Week", "Report"])

#     # Read the contents of both CSV files
#     df1 = pd.read_csv(file1)
#     df2 = pd.read_csv(file2)

#     # Merge the DataFrames based on the user ID column
#     merged_df = pd.merge(df1, df2, on='User ID', how='outer')

#     # Append the merged DataFrame to the output CSV file
#     merged_df.to_csv(output_file, index=False, mode='a', header=False)

# # Main program
# file1 = 'Data/Student_data.csv'  # Path to the first CSV file
# file2 = 'Data/Students_report.csv'  # Path to the second CSV file
# output_file = 'Data/merged_file.csv'  # Path to the output merged CSV file

# append_csv_files(file1, file2, output_file)
