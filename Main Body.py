import re
import login

print("Welcome to Summer Internship Portal\nPlease log in")

print()

print("User ID  guide\nFor student: 'STUD' followed by Registration Number (STUD2345678)\nFor Internship Guide: 'IG' followed by Employee ID (IG2345)\nFor Admin: 'A' followed by Employee ID (A2345)")
user = input("Enter your User ID: ")
if re.match(r"^(STUD)", user):
    login.student_login(user)
    user_is = "S"
elif re.match(r"^(IG)", user):
    login.guide_login(user)
    user_is = "IG"
elif re.match(r"^(A)", user):
    login.admin_login(user)
    user_is = "A"
else:
    print("Enter a vaild input")
