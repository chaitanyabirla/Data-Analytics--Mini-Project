# from numpy import NaN
# import pandas as pd

# def generate_guide_data():
#     guide_list = []
#     for i in range(2201,2216):
#        j = [i,'christ@'+str(i),NaN,NaN,NaN]
#        guide_list.append(j)
#     guide_data= pd.DataFrame(guide_list, columns=['User ID', 'Password','Department','Name','Announcement'])
#     return guide_data,guide_list

# guide_data,_ = generate_guide_data()
# guide_data.to_csv("Data/Guide_data.csv",index = False)


# def generate_student_id():
#     student_list = []
#     for i in range(2211200,2211700):
#        j = [i,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN]
#        student_list.append(j)
#     student_data= pd.DataFrame(student_list, columns=['User ID', 'Password','Name', 'Year', 'Department', 'Course','Week 1 Report','Week 2 Report','Week 3 Report','Week 4 Report','Week 5 Report','Week 6 Report','Final Report'])
#     return student_data,student_list
# generate_student_id()

# student_data,_ = generate_student_id()
# student_data.to_csv("Data/Student_data.csv",index = False)

# def generate_reports_data():
#     report_list = []
#     for i in range(2211200,2211700):
#        j = [i,NaN,NaN,NaN,NaN,NaN,NaN,NaN]
#        report_list.append(j)
#     report_data= pd.DataFrame(report_list, columns=['User ID', 'Week 1 Report','Week 2 Report','Week 3 Report','Week 4 Report','Week 5 Report','Week 6 Report','Final Report'])
#     return report_data, report_list

# report_data,_ = generate_reports_data()
# report_data.to_csv("Data/Report_data.csv",index = False)
