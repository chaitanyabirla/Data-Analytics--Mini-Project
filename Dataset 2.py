import openpyxl

wb = openpyxl.load_workbook("dataset.xlsx")

# Access the worksheet
ws = wb["student_details"]

# Write the value in the cell
ws["A2"] = "Chaitanya"

# Save the workbook
wb.save("database.xlsx")