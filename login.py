import pandas as pd
#function to log in a student
def student_login():  
    user = int(input("Enter your User ID: "))  
    print()   
    # Read the student data from a csv file                            
    dataset = pd.read_csv("Data/Student_data.csv")                     
    # Check if the user ID is valid
    if user in dataset['User ID'].values:
        # Check if the password is set or not
        if pd.isna(dataset.loc[dataset['User ID'] == user, 'Password'].values[0]):
            # Ask the user to set a password
            stud_Pswd = input("Set Password: ")
            if input("Confirm Password: ") == stud_Pswd:
                # Update the student data with the password
                dataset.loc[dataset['User ID'] == user, 'Password'] = stud_Pswd
                dataset.to_csv("Data/Student_data.csv", index=False)
                print()
                print('*'*50)
                print(f"{'Logged In Successfully!' : ^50}")
                print('*'*50)
                print()
                status = True
            else:
                 # Print an error message if passwords do not match
                print("Passwords did not match\nRe-enter") 
                print()
                status = False
        else:
            # Ask the user to enter the password
            stud_Pswd = input("Enter Password: ")  
            if (dataset.loc[dataset['User ID'] == user, 'Password'] == stud_Pswd).any():
                print()
                print('*'*50)
                print(f"{'Logged In Successfully!' : ^50}")
                print('*'*50)
                print() 
                status = True
            else:
                # Print an error message if password is incorrect
                print("Password did not match\nRe-enter")
                print()
                status = False
    else:
        # Print an error message if user ID is invalid
        print("Enter a vaild User ID")
        print()
        status = False
    return status, user, dataset 


#function to log in a guide
def guide_login():
    user = int(input("Enter your User ID: "))
    print()
    guide_UserId = user
    dataset = pd.read_csv("Data/Guide_data.csv")
    
     # Check if the user ID is valid
    if guide_UserId in dataset['User ID'].values:
        guide_Pswd = input("Enter Password: ")
        # Check if the password is correct
        if (dataset.loc[dataset['User ID'] == user, 'Password'] == guide_Pswd).any():
            print()
            print('*'*50)
            print(f"{'Logged In Successfully!' : ^50}")
            print('*'*50)
            print()
            status = True
        else:
            # Print an error message if password is incorrect
            print("Password did not match\nRe-enter")
            print()
            status = False
    else:
        print("Enter a valid User ID")
        print()
        status = False
    
    # Return the status, user ID and guide data
    return status, user, dataset
