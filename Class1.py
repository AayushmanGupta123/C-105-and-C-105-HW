import csv

with open('SD/graphs/class1.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
totalMarks = 0
totalEntries = len(fileData)
for marks in fileData:
    totalMarks += float(marks[1])

mean = totalMarks/totalEntries
print("Mean = "+ str(mean))

import pandas as pd
import plotly.express as px


file = pd.read_csv("SD/graphs/class1.csv")
fig = px.scatter(file,x = "Student Number",y = "Marks", title = "Marks Of Class1")
fig.update_layout(shapes = [
    dict(type = 'line',y0 = mean,y1 = mean,x0 = 0,x1 = totalEntries)
])
fig.update_yaxes(rangemode = "tozero")
fig.show()