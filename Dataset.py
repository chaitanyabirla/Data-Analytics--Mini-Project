from numpy import NaN
import pandas as pd

def generate_guide_data():
    guide_list = []
    for i in range(2201,2216):
       j = [i,'christ@'+str(i)]
       guide_list.append(j)
    guide_data= pd.DataFrame(guide_list, columns=['User ID', 'Password'])
    return guide_data

'''
    with open('guide_UserId.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Guide ID'])
     for id in guide_ids:
        writer.writerow([id])
'''

def generate_admin_data():
    admin_list = []
    for i in range(2201,2204):
       j = [i,'christ@'+str(i)]
       admin_list.append(j)
    admin_data= pd.DataFrame(admin_list, columns=['User ID', 'Password'])
    return admin_data

'''
    with open('admin_UserId.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Admin ID'])
     for id in admin_ids:
        writer.writerow([id])
'''

def generate_student_id():
    student_list = []
    for i in range(2211200,2211700):
       j = [i,NaN]
       student_list.append(j)
    student_data= pd.DataFrame(student_list, columns=['User ID', 'Password'])
    return student_data, student_list

print(generate_student_id())

import pandas as pd

def generate_student_id_modified():
    student_list = []
    for i in range(2211200, 2211700):
        j = [i, pd.NA]
        student_list.append(j)
    student_data = pd.DataFrame(student_list, columns=['User ID', 'Password'])
    return student_data



'''
    with open('student_UserId.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Student ID'])
     for id in student_id_:
        writer.writerow([id])   
'''
