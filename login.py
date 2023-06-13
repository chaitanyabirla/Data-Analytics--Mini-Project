from numpy import NaN
import pandas as pd
import Dataset

def student_login(user):                                    #here we need to save things in a csv file!
    dataset,_ = Dataset.generate_student_id()                         
    if user in dataset['User ID'].values:
        if pd.isna(dataset.loc[dataset['User ID'] == 2211200, 'Password'].values[0]):
            stud_Pswd = input("Set Password: ")
            if input("Confirm Password: ") == stud_Pswd:
                dataset.loc[dataset['User ID'] == user, 'Password'] = stud_Pswd
                print("Loged In Successfully!")
            else:
                print("Passwords did not match\nRe-enter") 
        else:
            stud_Pswd = input("Enter Password: ")   
    else:
        print("Enter a vaild User ID")
    return True                                                         

def guide_login(user):
    guide_UserId = user
    dataset = Dataset.generate_guide_id()                       
    if guide_UserId in dataset['User ID'].values:                 
        guide_Pswd = input("Enter Password: ") 
    else: 
        print("Enter a vaild User ID")
    return True

def admin_login(user):
    admin_UserId = user
    dataset = Dataset.generate_admin_id()
    if admin_UserId in dataset['User ID'].values:                 
        admin_Pswd = input("Enter Password: ") 
    else: 
        print("Enter a vaild User ID")
    return True
