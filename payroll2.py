"""
Program: payroll2.py
Chapter 4 practice project (133)

Payroll appication that reads employee data from a text time and outputs payroll info in a tabular format.
"""
import os.path
import time

#region Get input file path from user
filename = input("Please type the name of the payroll file you wish to process >> ")
# filename = "payroll_data.txt"

while not os.path.isfile(filename):
    filename = input("Sorry! Please input a VALID file name >> ")
#endregion 
#region Set up table
print("Processing file data...")
time.sleep(3)

print("\n%-18s%9s%9s%11s" % ("Last Name", "Wage", "Hours", "Earnings"))
print("-" * 50)
#endregion
with open(filename, 'r') as data: #Print table data
    for line in data:
        lineArray = line.split() #[name, wage, hours]
        [name, wage, hours] = line.split()
        wage, hours = float(wage), float(hours)
        print(f"{name:18s}{wage:9.2f}{hours:9.2f}{wage*hours:11.2f}")

input("\n\nEnd of file. Press ENTER to quit.")