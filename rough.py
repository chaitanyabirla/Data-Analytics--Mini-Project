from numpy import NaN
import Dataset
import pandas as pd

import pandas as pd

def student_registration():
    regnum = input("Enter your registration number: ")
    database = Dataset.generate_student_data_modified()

    # Create a DataFrame from the database list
    df = pd.DataFrame(index=range(database), columns=['Registration Number', 'Name', 'Course Name', 'Year', 'Course'])
    combined_df = pd.concat([df, database], axis=0)
    print(database)
    print(df)
    print(combined_df)
    # Find the row with the matching registration number
    matching_row = df.loc[df['Registration Number'] == regnum]

    if not matching_row.empty:
        # Update the values in the matching row
        matching_row.loc[:, 'Name'] = input("Enter your name: ")
        matching_row.loc[:, 'Course Name'] = input("Enter the course name: ")
        matching_row.loc[:, 'Year'] = int(input("Enter the year you are studying in: "))
        matching_row.loc[:, 'Course'] = input("Enter your class (For e.g: 2LLB-A): ")

        # Convert the DataFrame back to a list
        updated_database = df.values.tolist()
    else:
        print("Invalid registration number.")
        updated_database = database  # Keep the original database as it is

    return updated_database

student_data = student_registration()
print(student_data)
