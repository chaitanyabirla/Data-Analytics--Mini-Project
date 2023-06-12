import pandas
import csv

for i in range(2201,2250):
    teacher_ids=[].append 
with open('guide_UserId.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student ID'])
    for id in teacher_ids:
        writer.writerow([id])


def generate_admin_id():
    x = random.randint(1,5)
    y=''
    if x<=5:
        y = "0" + str(x)
    return y



