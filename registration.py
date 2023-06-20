# Import the pandas library
import pandas as pd
# Import the Dataset module
import Data.Dataset as Dataset
# Import the NaN constant from numpy
from numpy import NaN

# a function to register a guide
def guide_registration(userid):
    # Initialize a flag to False
    flag = False
    database = pd.read_csv("Data/Guide_data.csv")
    # Convert the data to a list of lists
    datalist = database.values.tolist()

     # Loop through the data list
    for i in range(len(datalist)):
        # Check if the user ID matches with any record
        if datalist[i][0] == userid:
             # Ask the user to enter their name and department
            name = input("Enter our Name: ")
            department = input("Enter your Department: ")
            # Update the data list with the name and department
            datalist[i][2] = name
            datalist[i][3] = department
            flag = True# Set the flag to True
            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()
            break
    
     # If the flag is still False, print an error message
    if not flag:
        print("Invalid registration number!")

     # Convert the data list back to a data frame with column names
    database = pd.DataFrame(datalist, columns=['User ID', 'Password', 'Name', 'Department', 'Announcement'])
     # Save the updated data frame to the csv file
    database.to_csv("Data/Guide_data.csv", index=False)
    return database # Return the updated data frame


#a function to register a student
def student_registration(regnum):
    flag = False
    database = pd.read_csv("Data/Student_data.csv")
    datalist = database.values.tolist()

    # Loop through the data list
    for i in range(len(datalist)):
        # Check if the registration number matches with any record
        if datalist[i][0] == regnum:
            # Ask the user to enter their name, year, course and department
            name = input("Enter Your Name: ")
            year = int(input("Enter the Year you are Studying in: "))
            course = input("Enter Your Course: ")
            department = input("Enter Your Department: ")
            # Update the data list with the name, year, course and department
            datalist[i][2] = name
            datalist[i][3] = year
            datalist[i][4] = department
            datalist[i][5] = course
            flag = True
            break

    if not flag:
        print("Invalid registration number!")

    database = pd.DataFrame(datalist, columns=['User ID', 'Password', 'Name', 'Year', 'Department', 'Course','Week 1 Report','Week 2 Report','Week 3 Report','Week 4 Report','Week 5 Report','Week 6 Report','Final Report'])
    # Save the updated data frame to the csv file 
    database.to_csv("Data/Student_data.csv", index=False)
    return database


#function to register an internship for a student 
def internship(regnum):
    intern_detail_list=[]
    # Loop through a range of user IDs 
    for i in range(2211200,2211700):
        # Create a sublist with user ID and NaN values for other fields 
        j=[i,NaN,NaN,NaN,NaN,NaN,NaN]
        # Append the sublist to the intern detail list 
        intern_detail_list.append(j)
    
    flag=False
    for i in range(len(intern_detail_list)):
        # Check if the registration number matches with any record 
        if intern_detail_list[i][0] == regnum:
            # Ask the user to enter their company name, domain, weeks of work, guide name, guide email and guide designation 
            company = input("Enter the Company Name: ")
            domain = input("Enter the Domain in which you are doing your Internship: ")
            weeks = int(input("Enter the Number of Weeks of Internship: "))
            guide_name = input("Enter your Company Guide's Name: ")
            guide_email = input("Enter your Guide's Email ID: ")
            guide_designation = input("Enter your Guide's Designation: ")
            
            # Update the intern detail list with the user inputs
            intern_detail_list[i][1]=company
            intern_detail_list[i][2]=domain
            intern_detail_list[i][3]=weeks
            intern_detail_list[i][4]=guide_name
            intern_detail_list[i][5]=guide_email
            intern_detail_list[i][6]=guide_designation
            flag=True

            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()

            break
        # print an error message
    if not flag:
        print("Invalid registration number!")
    
    # Convert the intern detail list to a data frame with column names  
    intern_data= pd.DataFrame(intern_detail_list, columns=['User ID',"Company Name" , "Domain" , "Weeks of Work" , "Guide Name" , "Guide Email" , "Guide Designation"])
    return intern_data


#function to register a coursework for a student
def coursework(regnum): 
     # Import the datetime module
    from datetime import datetime
    course_detail_list=[]
    for i in range(2211200,2211700):
        # Create a sublist with user ID and NaN values for other fields 
        j=[int(i),NaN,NaN,NaN,NaN,NaN,NaN]
        course_detail_list.append(j)
    
    flag=False
    for i in range(len(course_detail_list)):
        # Check if the registration number matches with any record 
        if course_detail_list[i][0] == regnum:
            # Ask the user to enter their course name, domain, start date, end date, guide name and guide email 
            course_name = input("Enter the Course Name: ")
            domain = input("Enter the Domain of your Course: ")
            start = input("Enter Start Date (YYYY-MM-DD): ")
            start_date=datetime.strptime(start, "%Y-%m-%d")
            end = input("Enter End Date (YYYY-MM-DD): ")
            end_date=datetime.strptime(end, "%Y-%m-%d")
            instructor_email = input("Enter your Course Instructor's Email ID: ")
            instructor_designation = input("Enter your instructor's Designation: ")
            
            # Update the course detail list with the user inputs
            course_detail_list[i][1] = course_name
            course_detail_list[i][2] = domain
            course_detail_list[i][3] = start_date
            course_detail_list[i][4] = end_date
            course_detail_list[i][5] = instructor_email
            course_detail_list[i][6] = instructor_designation
            flag=True

            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()

            break
        #flag is still False, print an error message
    if not flag:
        print("Invalid registration number!")
        #Convert the course detail list to a data frame with column names
    course_data= pd.DataFrame(course_detail_list, columns=['User ID',"Course Name" , "Domain" , "Start Date" , "End Date" , "Instructor Email" , "Instructor Designation"])
    return course_data# Return the course data frame

# Define a function to register a research work for a student
def Reserchwork(regnum):
    from datetime import datetime
    reserch_detail_list=[]
    for i in range(2211200,2211700):
        # Create a sublist with user ID and NaN values for other fields 
        j=[int(i),NaN,NaN,NaN,NaN,NaN,NaN,NaN]
        reserch_detail_list.append(j)
    
    flag=False
      # Loop through the research detail list 
    for i in range(len(reserch_detail_list)):
        # Check if the registration number matches with any record  
        if reserch_detail_list[i][0] == regnum:
            # Ask the user to enter their university name, domain, start date, end date, guide email, guide designation and publication name
            university = input("Enter the University in which you are doing Research: ")
            domain = input("Enter the Domain of your Reserch: ")
            start = input("Enter Start Date (YYYY-MM-DD): ")
            start_date=datetime.strptime(start, "%Y-%m-%d")
            end = input("Enter End Date (YYYY-MM-DD): ")
            end_date=datetime.strptime(end, "%Y-%m-%d")
            guide_email = input("Enter your University Guide's Email ID: ")
            guide_designation = input("Enter ypur Guide's designation: ")
            publication=input("Enter the Name of Publication in which your Reserch is getting Published: ")
            

            # Update the research detail list with the user inputs 
            reserch_detail_list[i][1]=university
            reserch_detail_list[i][2]=domain
            reserch_detail_list[i][3]=start_date
            reserch_detail_list[i][4]=end_date
            reserch_detail_list[i][5]=guide_email
            reserch_detail_list[i][6]=guide_designation
            reserch_detail_list[i][7]=publication
            flag=True

            print()
            print("*"*50)
            print(f"{'Registered Successfully!' : ^50}")
            print("*"*50)
            print()

            break
    if not flag:
        print("Invalid registration number.")
        # Convert the research detail list to a data frame with column names
    reserch_data= pd.DataFrame(reserch_detail_list, columns=['User ID',"University Name" , "Domain" , "Start Date" , "End Date" , "Guide Email" , "Guide Designation","Publication"])
    return reserch_data

#function to merge student data and internship data and save it to a csv file
def stu_intern(user,database):
    intern_data = internship(user)# Call the internship function and get the internship data frame 
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Intern_data.csv", index=False)# Save the merged data frame to a csv file 

#a function to merge student data and course data and save it to a csv file 
def stu_course(user,database):
    intern_data = coursework(user)
    # Merge the student data and course data on user ID using outer join 
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Course_data.csv", index=False)


#a function to merge student data and research data and save it to a csv file 
def stu_reserch(user,database):
    intern_data = Reserchwork(user)
    appended_data = pd.merge(database, intern_data, on='User ID', how='outer')
    appended_data.to_csv("Data/Reserch_data.csv", index=False)