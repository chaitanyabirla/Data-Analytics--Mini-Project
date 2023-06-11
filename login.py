## IMPORTS
import re

## USER DEF FUNCTIONS
def student_login(user):
    stud_UserId = user                          ##Need to see how to save these in a file!!
    if stud_UserId in dataset:
        stud_Pswd = input("Enter Password: ")   ##Need to think passwrd safety!
    else: 
        stud_Pswd = input("Set Password: ")
        if input("Confirm Password: ") == stud_Pswd:
            print("Loged In Successfully!")
        else:
            print("Passwords did not match\nRe-enter")

def guide_login(user):
    guide_UserId = user
    if guide_UserId in dataset:                 ##Need to see how to save these in a file!!
        guide_Pswd = input("Enter Password: ") 
    else: 
        print("Enter a vaild User ID")

def admin_login(user):
    admin_UserId = user
    if admin_UserId in dataset:                 ##Need to see how to save these in a file!!
        admin_Pswd = input("Enter Password: ") 
    else: 
        print("Enter a vaild User ID")


## MAIN BODY

# Log in
print("Welcome to Summer Internship Portal\nPlease log in")

print()

print("User ID  guide\nFor student: 'STUD' followed by Registration Number (STUD2345678)\nFor Internship Guide: 'IG' followed by Employee ID (IG2345)\nFor Admin: 'A' followed by Employee ID (A2345)")
user = input("Enter your User ID: ")
if re.match(r"^(STUD)", user):
    student_login(user)
    user_is = "S"
elif re.match(r"^(IG)", user):
    guide_login(user)
    user_is = "IG"
elif re.match(r"^(A)", user):
    admin_login(user)
    user_is = "A"
else:
    print("Enter a vaild input")

#user = input("Enter:\n 'S' to log in as a Student\n'IG' to log in as an Internship Guide\n'A' to log in as an Admin").upper()
#if user == "S":
#    student_login()
#elif user == "IG":
#    guide_login()
#elif user == "A":
#    admin_login()
#else:
#    print("Enter a vaild input")