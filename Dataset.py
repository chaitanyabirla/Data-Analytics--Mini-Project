import random
import csv

def generate_student_id():
    return 'STUD' + str(range(100, 999))

student_ids = [generate_student_id() for i in range(500)]

with open('student_ids.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student ID'])
    for id in student_ids:
        writer.writerow([id])



def generate_teacher_id():
    x = random.randint(1,50)
    y=''
    if x<10:
        y = "0" + str(x)
    else:
        y = str(x)
    return y

teacher_ids=[generate_teacher_id() for i in range(500)]


def generate_admin_id():
    x = random.randint(1,5)
    y=''
    if x<=5:
        y = "0" + str(x)
    return y



