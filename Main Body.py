import Dataset
import login
import registration
import guide
import pandas as pd

print('*'*25)
print("Welcome to Summer Internship Portal\nPlease log in")
print('*'*25)

print()

print("Log in Guide\nFor student: 'STUD'\nFor Internship Guide: 'IG'")
user_is = input("Log in as: ").upper()


if user_is == "STUD":
    status=True
    while status == True:
        result,_ = login.student_login()
        if result:
            _,user = login.student_login
            dataset,_ = Dataset.generate_student_id()
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                registration.student_registration(user) 
            announcement_result, announcement = guide.announce()
            if announcement_result:
                print("There is an announcement!!")
                print(announcement)
            status = False
        else:
            status = True
    
elif user_is == "IG":
    status=True
    while status == True:
        result,_ = login.guide_login()
        if result:
            _,user = login.guide_login
            dataset,_ = Dataset.generate_student_id()
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                registration.Guide_registration()
            print("You can use the following functions:\n'View': To view the records of all students\n'View Student Specific': To view the records of specific students\n'Type': To see how many students have opted for internship, research and coursework\n'") 
            status = False
        else:
            status = True
    
else:
    print("Enter a vaild input")   #only problem here :) and i dont wanna solve this
