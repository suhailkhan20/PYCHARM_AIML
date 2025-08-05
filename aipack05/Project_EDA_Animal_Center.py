# Project_EDA_Animal_Center.py
'''
DataAnalytics Project: EDA Animal Care Center
--------------------------------------------

Project Task-10: What are the conditions of animals which are taken into the shelter?

Project Task-11: How many types of animals are taken into shelter and what is their total count?

Project Task-12: what are the top 10 breeds in the animal shelter?
         Draw a breed wise bar plot.

Project Task-13: What are top 20 common names of animals in animal shelter?
         Draw a bar char reprsenting name wise count of the animals.

Project Task-14: Draw a bar char representing the "Outcome Type" wise count of animals using the dataset of Animal_Center_Outcomes.csv.
'''


#Project Task-01: Print the shape of the dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

intake = pd.read_csv('DataSet_Animal_Center_Intakes.csv')
outcome = pd.read_csv('DataSet_Animal_Center_Outcomes.csv')

print("intake.shape = ", intake.shape)
print("outcome.shape = ", outcome.shape)
print("\n")
print("intake.head = ", intake.head)

#Project Task-02: Which column has null values?

plt.subplots(figsize=(8,6))
sns.heatmap(intake.isnull())
plt.show()

#Project Task-03: Remove the duplicate rows from intake dataset.
print("\n\n")
print("Total duplicated rows =", intake.duplicated().sum())

intake.drop_duplicates(inplace=True)
print("Duplicate rows deleted from intake animal center")

print("intake.shape = ", intake.shape)



'''
Project Task-04: Rename to column names as follows:-
1) 'Old Column Name' = 'New Column Name'
2) 'Animal ID'        =  'id',
3) 'DateTime'         =  'date_time',
4) 'MonthYear'        =  'month_year',
5) 'Found Location'   = 'found_location',
6) 'Intake Type'      = 'intake_type',
7) 'Intake Condition' = 'intake_condition',
8) 'Animal Type'      = 'animal_type',
9) 'Sex upon Intake'  = 'sex_upon_intake',
10) 'Age upon Intake' = 'age_upon_intake',
11) 'Breed'           =  'breed'
'''

print("Before renaming the column headings :\n", intake.columns)

intake.rename(columns={'Animal ID':'id',
                       'DateTime':'date_time',
                       'MonthYear':'month_year',
                       'Found Location':'found_location',
                       'Intake Type':'intake_type',
                       'Intake Condition':'intake_condition',
                       'Animal Type':'animal_type',
                       'Sex upon Intake':'sex_upon_intake',
                       'Age upon Intake':'age_upon_intake',
                       'Breed':'breed'},  inplace=True)

print("After renaming the column headings :\n", intake.columns)


#Project Task-05: Remove Monthyear column because it is similar to Datetime column.
intake.drop('month_year', axis=1, inplace=True)
print("After drop month year column\n\n",intake.head())
print("\n")

#Project Task-06: Extracting month and year from Datetime column
intake['date_time'] = intake['date_time'].astype('datetime64[ns]')
intake['year'] = intake['date_time'].dt.year
intake['month'] = intake['date_time'].dt.month
print("After extracting month, year from Datetime column:\n", intake.head())


#Project Task-07: Which month,year has most animal intakes ?
        # Draw a pie chart representing year wise animal intake from year 2014 to 2021.
# Plot year-wise intake distribution as pie chart
plt.subplots(figsize=(10, 8))
print("intake['year'].value_counts() = \n", intake['year'].value_counts())
intake['year'].value_counts().plot(kind='pie', autopct='%.2f%%', shadow=True)
plt.show()


#Project Task-08: Create a bar chart to represent month wise animal intake.
         #Which month has heighest animal intake?
# May month has most animal intakes - plotting month-wise bar chart
plt.subplots(figsize=(10, 8))
plt.ylabel('Months')
intake['month'].value_counts().plot(kind='barh')
plt.show()


#Project Task-09: Create a bar chart to represent animal intake methods wise counting.
#         What are the animal intake methods ? Print their names?
plt.subplots(figsize=(10, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.title('Animal intake methods')
intake.groupby('intake_type')['id'].count().plot(kind='bar', color=colors)
plt.show()


print(intake.groupby('intake_type')['intake_condition'].value_counts())

# How many types of animals are taken into shelter and what is their total count
print(intake.groupby('intake_type')['animal_type'].value_counts())
plt.subplots(figsize=(10, 6))
color = ['#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
intake['breed'].value_counts().head(10).plot(kind='barh', color=color)

# What are top 20 common names of animals in animal shelter
plt.subplots(figsize=(12, 10))
color = ['#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
intake['Name'].value_counts().head(20).plot(kind='bar', color=color)


print(outcome.head())

print(outcome.head())
plt.subplots(figsize=(10, 8))
color = ['#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.xlabel('Outcome Type')
outcome['Outcome Type'].value_counts().plot(kind='bar', color=color)
plt.show()