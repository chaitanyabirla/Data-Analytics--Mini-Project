from numpy import NaN
import pandas as pd

def generate_guide_data():
    guide_list = []
    for i in range(2201,2216):
       j = [i,'christ@'+str(i)]
       guide_list.append(j)
    guide_data= pd.DataFrame(guide_list, columns=['User ID', 'Password'])
    return guide_data

def generate_admin_data():
    admin_list = []
    for i in range(2201,2204):
       j = [i,'christ@'+str(i)]
       admin_list.append(j)
    admin_data= pd.DataFrame(admin_list, columns=['User ID', 'Password'])
    return admin_data

def generate_student_id():
    student_list = []
    for i in range(2211200,2211700):
       j = [i,NaN,NaN,NaN,NaN,NaN,NaN]
       student_list.append(j)
    student_data= pd.DataFrame(student_list, columns=['User ID', 'Password'])
    return student_data, student_list
