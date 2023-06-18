from numpy import NaN
import pandas as pd
import Dataset

def student_login():  
    user = int(input("Enter your User ID: "))                                     #here we need to save things in a csv file!
    dataset = pd.read_csv("Student_data.csv")                     
    if user in dataset['User ID'].values:
        if pd.isna(dataset.loc[dataset['User ID'] == user, 'Password'].values[0]):
            stud_Pswd = input("Set Password: ")
            if input("Confirm Password: ") == stud_Pswd:
                dataset.loc[dataset['User ID'] == user, 'Password'] = stud_Pswd
                print("Loged In Successfully!")
                status = True
            else:
                print("Passwords did not match\nRe-enter") 
                status = False
        else:
            stud_Pswd = input("Enter Password: ")  
            if dataset.loc[dataset['User ID'] == user, 'Password'] == stud_Pswd:
                print("Loged In Successfully!") 
                status = True
            else:
                print("Password did not match\nRe-enter")
                status = False
    else:
        print("Enter a vaild User ID")
        status = False
    return status, user, dataset 

_,_,dataset = student_login()
dataset.to_csv("Student_data.csv", index=True)

'''
def guide_login():
    user = int(input("Enter your User ID: "))
    guide_UserId = user
    dataset = pd.read_csv("Guide_data.csv")                      
    if guide_UserId in dataset['User ID'].values:                 
        guide_Pswd = input("Enter Password: ") 
        if dataset.loc[dataset['User ID'] == user, 'Password'] == guide_Pswd:
            print("Loged In Successfully!") 
            status = True
        else:
            print("Password did not match\nRe-enter")
            status = False 
    else: 
        print("Enter a vaild User ID")
        status = False
    return status, user
'''
def guide_login():
    user = int(input("Enter your User ID: "))
    guide_UserId = user
    dataset = pd.read_csv("Guide_data.csv")
    
    if guide_UserId in dataset['User ID'].values:
        guide_Pswd = input("Enter Password: ")
        
        if (dataset.loc[dataset['User ID'] == user, 'Password'] == guide_Pswd).any():
            print("Logged In Successfully!")
            status = True
        else:
            print("Password did not match\nRe-enter")
            status = False
    else:
        print("Enter a valid User ID")
        status = False
    
    return status, user, dataset

_,_,dataset = guide_login()
dataset.to_csv("Guide_data.csv", index=True)
