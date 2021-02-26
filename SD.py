import math
import csv

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
totalMarks = 0
totalEntries = len(fileData)
for marks in fileData:
    totalMarks += float(marks[1])

mean = totalMarks/totalEntries
print("Mean = "+ str(mean))