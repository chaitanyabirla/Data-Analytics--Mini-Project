import pandas as pd

def student_login():  
    user = int(input("Enter your User ID: "))  
    print()                               
    dataset = pd.read_csv("Data/Student_data.csv")                     
    if user in dataset['User ID'].values:
        if pd.isna(dataset.loc[dataset['User ID'] == user, 'Password'].values[0]):
            stud_Pswd = input("Set Password: ")
            if input("Confirm Password: ") == stud_Pswd:
                dataset.loc[dataset['User ID'] == user, 'Password'] = stud_Pswd
                dataset.to_csv("Data/Student_data.csv", index=False)
                print()
                print('*'*50)
                print(f"{'Logged In Successfully!' : ^50}")
                print('*'*50)
                print()
                status = True
            else:
                print("Passwords did not match\nRe-enter") 
                print()
                status = False
        else:
            stud_Pswd = input("Enter Password: ")  
            if (dataset.loc[dataset['User ID'] == user, 'Password'] == stud_Pswd).any():
                print()
                print('*'*50)
                print(f"{'Logged In Successfully!' : ^50}")
                print('*'*50)
                print() 
                status = True
            else:
                print("Password did not match\nRe-enter")
                print()
                status = False
    else:
        print("Enter a vaild User ID")
        print()
        status = False
    return status, user, dataset 



def guide_login():
    user = int(input("Enter your User ID: "))
    print()
    guide_UserId = user
    dataset = pd.read_csv("Data/Guide_data.csv")
    
    if guide_UserId in dataset['User ID'].values:
        guide_Pswd = input("Enter Password: ")
        if (dataset.loc[dataset['User ID'] == user, 'Password'] == guide_Pswd).any():
            print()
            print('*'*50)
            print(f"{'Logged In Successfully!' : ^50}")
            print('*'*50)
            print()
            status = True
        else:
            print("Password did not match\nRe-enter")
            print()
            status = False
    else:
        print("Enter a valid User ID")
        print()
        status = False
    
    return status, user, dataset
