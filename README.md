# Data-Analytics--Mini-Project

## Summer Internship Portal

### Collaborators
* Chaitanya Birla (Reg No 22112312)
  
  https://github.com/chaitanyabirla

* Kanishk Saleria (Reg No 22112317)
  
  https://github.com/kanishksaleria

### Description
This mini project has been developed by us as part of the course 'Data Analytics with Mini Project' in our 3rd Semester of BSc Economics and Analytics at Christ (Deemed to be University).

This project is a **Summer Internship Portal** to manage the internship for the students at Christ. The portal allows students to log in and enter their personal and academic details. It also enables the guides to monitor and manage the students’ data.  

This portal has been made Menu-based using Python, File Handling to store and access data stored in a csv file and Pandas for data manipulation. It also uses user-defined functions to perform various tasks, such as validating the user input and displaying the menu options. It is designed to be user-friendly, interactive, and secure.

### Functionality
This portal provides you two login options: **Student** and **Internship Guide**

#### Student
* The students will be first asked to `login` with their User IDs and passwords. If they are logging in for the first time, they will be asked to set a password.
* For their first login, they guided to the `registration` menu where they will have to fill in their details, including their year of study, department and course. Then they will be guided to the `type` menu where they will have to select if they have opted for an internship, research work or course work and fill in the details accordingly.
* They will get the option to enter their weekly reports and if done with all 6 weekly reports, they can enter their final report.
* If an Internship Guide has made an announcement, students will be able to see once they login.

#### Internship Guide
* The internship guides will be first asked to `login` with their User IDs and passwords. For them the passwords have been set beforehand for security.
* For their first login, they guided to the `registration` menu where they will have to fill in their details: Name and Department.
* They will be guided to `functions` menu where they can use pre-defined functions to view and manage the students' data.
* They can also make announcements which will be visible to the students.

There have been seperate packages created for the different menus for easy and the main code has been saved in the **Main Body.py** file. The datasets have been stored under the **Data** folder in csv files.
