import pandas as pd
import login as lgin
import registration as reg
import guide as gud

print('*'*50)
print(f"{'Welcome to Summer Internship Portal' : ^50}")
print(f"{'Please log in' : ^50}")
print('*'*50)

print()

print("<<Log-in Guide>>\nFor student: 'STUD'\nFor Internship Guide: 'IG'")

print()

user_is = input("Log-in as: ").upper()
print()

if user_is == "STUD":
    status = True
    while status:
        result, user, dataset = lgin.student_login()
        if result:
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                print("You have loged in for the first time\nnYou need to register!")
                dataset = reg.student_registration(user)
            print()
            print("<<Type Guide>>\nIntership: 'IN'\nResearch work: 'RW'\nCourse work: 'CW'")
            print()
            type = input("What have your chosen? ").lower()
            print()
            if type == 'in':
                reg.stu_intern(user,dataset)
            elif type == 'rw':
                reg.stu_reserch(user,dataset)
            elif type == 'cw':
                reg.stu_course(user,dataset)
            else:
                print("Enter a vaild input")
            print()
            guide_data = pd.read_csv("Data/Guide_data.csv")
            if not guide_data['Announcement'].isna().any():
                print('*'*50)
                print("There is an Announcement!")
                print('*'*50)
                print(guide_data['Announcement'])
            status = False
        else:
            status = True
    
elif user_is == "IG":
    status = True
    while status:
        result, user, dataset = lgin.guide_login()
        if result:
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                print("You have loged in for the first time\nnYou need to register!")
                dataset = reg.Guide_registration(user)
            print() 
            print("<<Functions Guide>>\nTo view the records of all students: 'View'\nTo view the records of specific students: 'View Student Specific'\nTo see how many students have opted for internship, research, and coursework: 'Type'\nTo see which course has been opted by most students: 'Popular Course'\nTo see which domain has been opted by most students: 'Popular Domain'\nTo see which students have submitted the needed documents: 'Submitted'\nTo make an announcement: 'Announcement'")
            print()
            status1 = True
            while status1:
                fun = input("Enter the function:").lower()
                if fun == "view":
                    gud.view_dataset()
                elif fun == "view student specific":
                    gud.view_student_records()
                elif fun == "type":
                    gud.view_type()
                elif fun == "popular course":
                    gud.popular_course()
                elif fun == "popular domain":
                    gud.popular_domain()
                elif fun == "submitted":
                    gud.students_submitted()
                elif fun == "announcement":
                    gud.announce(user)
                else:
                    print("Enter a valid function")
                print()
                
                print("<<Repeat Guide>>\nTo Continue: 'y'\nTo Exit: 'n'")
                print()
                repeat = input("Do you want to continue? ").lower()
                if repeat == "y":
                    continue
                else:
                    status1 = False
            status = False
        else:
            status = True
else:
    print("Enter a valid input")
