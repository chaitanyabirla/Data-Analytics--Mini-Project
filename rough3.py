import pandas as pd
import os.path
import csv

def enter_report():
    student_id = input("Enter your User ID: ")
    week = int(input("Enter week number: "))
    report = input("Enter report: ")

    csv_file_path = "Data/Students_report.csv"

    # Check if the file exists, if not, write the column headers
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["User ID"])

    # Append the report to the CSV file
    with open(csv_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, week, report])

    print("Report entered successfully!")


def merge_files(input_file, output_file):
    # Read the contents of the existing data file
    existing_data = pd.read_csv(input_file)

    # Create a new DataFrame with columns for all six weeks
    new_data = pd.DataFrame(columns=["User ID", "Week1", "Week2", "Week3", "Week4", "Week5", "Week6"])

    # Merge the new data with the existing data based on the user ID
    merged_data = pd.merge(existing_data, new_data, on="User ID", how="outer")

    # Save the merged data to the output file
    merged_data.to_csv(output_file, index=False)


print("Welcome to the Weekly Report System")

while True:
    print("\nMenu:")
    print("1. Enter Report")
    print("2. Merge Files")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        enter_report()
    elif choice == "2":
        input_file = "Data/Student_data.csv"
        output_file = "Data/Merged_data.csv"
        merge_files(input_file, output_file)
        print("Files merged successfully!")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Weekly Report System!")
