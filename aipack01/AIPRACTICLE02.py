#Practical-02
# 1.Load CSV Using Python Standard Library

import csv

# filename = open("C:\\Users\\suhai\\PycharmProjects\\MIS_DATA\\indians-diabetes.data.csv")
filename = open("D:\\Java DSA")
reader = csv.reader(filename, delimiter=',')

lines = list(reader)

print('No of Rows: ', len(lines), '\n\n')

print("List of Data \n", lines )