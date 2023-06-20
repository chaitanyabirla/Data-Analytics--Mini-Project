import pandas as pd
import login as lgin
import registration as reg
import guide as gud
import report as rep

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
                print("You have loged in for the first time\nYou need to register!")
                print()
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

            guide_data = pd.read_csv("Data/Guide_data.csv")     #this is not showing
            if not guide_data['Announcement'].isna().any():
                print('*'*50)
                print("There is an Announcement!")
                print('*'*50)
                print(guide_data['Announcement'])

            print("<<Weekly Report Guide>>\nTo Submit: 'y'\nTo Exit: 'n'")
            print()

            submit = input("Do you want to submit your Weekly Reports? ").lower()
            print()

            if submit == 'y':
                while True:
                    rep.weekly_report(user) 
                    break

            if not pd.isna(dataset.loc[dataset['User ID'] == user, 'Week 6 Report'].values[0]):      
                submit = input("Do you want to submit your Final Reports? ").lower()
                print()

                if submit == 'y':
                    while True:
                        rep.final_report(user)
                        break
                
            print('*'*55)
            print(f"{'Thank you for using the Summer Internship Portal!' : ^55}")
            print('*'*55)
            status = False
        else:
            status = True
    
elif user_is == "IG":
    status = True
    while status:
        result, user, dataset = lgin.guide_login()
        if result:
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                print("You have loged in for the first time\nYou need to register!")
                print()
                dataset = reg.guide_registration(user) 
            status1 = True
            while status1:
                print("<<Function Guide>>\nTo view the records of all students: 'View'\nTo view the records of specific students: 'View Student Specific'\nTo see how many students have opted for internship, research, and coursework: 'Type'\nTo see which course has been opted by most students: 'Popular Course'\nTo see which domain has been opted by most students: 'Popular Domain'\nTo see which students have submitted the needed documents: 'Submitted'\nTo make an announcement: 'Announcement'")
                print()
                fun = input("Enter the function: ").lower()
                if fun == "view":
                    print(gud.view_dataset())
                elif fun == "view student specific":
                    print(gud.view_student_records())
                elif fun == "type":
                    print(gud.view_type())
                elif fun == "popular course":
                    print(gud.popular_course())
                elif fun == "popular domain":
                    print(gud.popular_domain())
                elif fun == "submitted":
                    print(gud.students_submitted())
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
            print("Thank you for using the Summer Internship Portal!")
            status = False
        else:
            status = True
else:
    print("Enter a valid input!")