import login
import registration

print('*'*25)
print("Welcome to Summer Internship Portal\nPlease log in")
print('*'*25)

print()

print("Log in Guide\nFor student: 'STUD'\nFor Internship Guide: 'IG'\nFor Admin: 'A'")
user_is = input("Log in as: ").upper()


if user_is == "STUD":
    status=True
    while status == True:
        if login.student_login():
            registration.student_registration() 
            status = False
        else:
            status = True
    
elif user_is == "IG":
    status=True
    while status == True:
        if login.guide_login():
            registration.Guide_registration() 
            status = False
        else:
            status = True
    
elif user_is == "A":
    status=True
    while status == True:
        if login.admin_login():
            registration.Admin_registration() 
            status = False
        else:
            status = True
    
else:
    print("Enter a vaild input")   #only problem here :) and i dont wanna solve this
