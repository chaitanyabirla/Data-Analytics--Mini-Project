import pandas
import csv

def generate_guide_id():
    teacher_ids = []
    for i in range(2201,2250):
     teacher_ids.append(i)

    with open('guide_UserId.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Guide ID'])
     for id in teacher_ids:
        writer.writerow([id])



def generate_admin_id():
    admin_ids = []
    for i in range(1,10):
     admin_ids.append(i)

    with open('admin_UserId.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Admin ID'])
     for id in admin_ids:
        writer.writerow([id])

def generate_student_id():
    student_id_ = []
    for i in range(2211200,2211700):
     student_id_.append(i)

    with open('student_UserId.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Student ID'])
     for id in student_id_:
        writer.writerow([id])
'''
generate_admin_id()
generate_guide_id()
generate_student_id()
'''