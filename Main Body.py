import pandas as pd

print('*'*25)
print("Welcome to Summer Internship Portal\nPlease log in")
print('*'*25)

print()

print("Log-in Guide\nFor student: 'STUD'\nFor Internship Guide: 'IG'")
user_is = input("Log-in as: ").upper()

if user_is == "STUD":
    status = True
    import login
    while status:
        result, user, dataset = login.student_login()
        import registration
        if result:
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                registration.student_registration(user)
            dataset.to_csv("Student_data.csv", index=True) 
            type = input("Have you chosen Intership (IN)\nResearch work (RW)\nCourse work (CW)? ").lower()
            if type == 'in':
                registration.stu_intern(user,dataset)
            elif type == 'rw':
                registration.stu_reserch(user,dataset)
            elif type == 'cw':
                registration.stu_course(user,dataset)
            else:
                print("Enter a vaild input")
            #import guide
            #announcement_result, announcement = guide.announce()
            #if announcement_result:
            #    print("There is an announcement!!")
            #    print(announcement)
            status = False
        else:
            status = True
    
elif user_is == "IG":
    status = True
    import login
    while status:
        result, user,dataset = login.guide_login()
        if result:
            import registration
            if pd.isna(dataset.loc[dataset['User ID'] == user, 'Name'].values[0]):
                registration.Guide_registration(user)
            print("You can use the following functions:\n'View': To view the records of all students\n'View Student Specific': To view the records of specific students\n'Type': To see how many students have opted for internship, research, and coursework\n'Popular Course': To see which course has been opted by most students\n'Popular Domain': To see which domain has been opted by most students\n'Submitted': To see which students have submitted the needed documents\n'Announcement': To make an announcement")
            status1 = True
            import guide
            while status1:
                fun = input("Enter the function:").lower()
                if fun == "view":
                    guide.view_dataset()
                elif fun == "view student specific":
                    guide.view_student_records()
                elif fun == "type":
                    guide.view_type()
                elif fun == "popular course":
                    guide.popular_course()
                elif fun == "popular domain":
                    guide.popular_domain()
                elif fun == "submitted":
                    guide.students_submitted()
                elif fun == "announcement":
                    guide.announce()
                else:
                    print("Enter a valid function")
                repeat = input("Do you want to use another function? (y/n) ").lower()
                if repeat == "y":
                    continue
                else:
                    status1 = False
            status = False
        else:
            status = True
else:
    print("Enter a valid input")
