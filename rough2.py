import csv

def enter_report():
    student_id = input("Enter you User ID: ")
    week = int(input("Enter week number: "))
    report = input("Enter report: ")

    # Open the CSV file in write mode
    with open("Data/Students_Data.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([student_id, week, report])
    
    print("Report entered successfully!")


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



