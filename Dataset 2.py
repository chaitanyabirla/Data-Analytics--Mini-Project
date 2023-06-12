
import openpyxl

wb = openpyxl.load_workbook("test.xlsx")

# Access the worksheet
ws = wb["Sheet1"]

# Write the value in the cell
ws["A1"] = "Hello"

# Save the workbook
wb.save("test.xlsx")