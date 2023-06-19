import csv

reviews = []

while True:
    student_id = input("Enter student ID: ")
    review = input("Enter review: ")
    reviews.append([student_id, review])
    another_review = input("Do you want to enter another review? (y/n) ")
    if another_review.lower() == "n":
        break

# Save reviews to a CSV file
with open("reviews.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Student ID", "Review"])
    writer.writerows(reviews)
