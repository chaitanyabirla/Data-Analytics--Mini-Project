import re
import login
import registration_detail
print("Welcome to Summer Internship Portal\nPlease log in")

print()

print("User ID  guide\nFor student: 'STUD' followed by Registration Number (STUD2345678)\nFor Internship Guide: 'IG' followed by Employee ID (IG2345)\nFor Admin: 'A' followed by Employee ID (A2345)")
user = input("Enter your User ID: ")
status = True

if re.match(r"^(STUD)", user):
    while status == True:
        if login.student_login(user[4:]):
            registration_detail.student_registration() 
            status = False
        else:
            status = True
    
elif re.match(r"^(IG)", user):
    while status == True:
        if login.guide_login(user[2:]):
            registration_detail.Guide_registration() 
            status = False
        else:
            status = True
    
elif re.match(r"^(A)", user):
    while status == True:
        if login.admin_login(user[2:]):
            registration_detail.Admin_registration() 
            status = False
        else:
            status = True
    
else:
    print("Enter a vaild input")
