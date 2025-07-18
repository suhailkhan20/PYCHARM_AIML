""" Assignment Task: Student Grade Statistics

Description:
Process grades of 10 students across 4 subjects (Math, Science, English, History).
Create a 10x4 array with random scores (0-100).

Compute and print the following reprts:"""

import numpy as np

# Task: Create a 10x4 NumPy array with random grades (0 to 100)
# 10 students × 4 subjects (Math, Science, English, History)
np.random.seed(1)  # For reproducibility
grades = np.random.randint(0, 101, size=(10, 4))
print("Student Grades:\n", grades)

# a) Task: Compute average grade per student (row-wise)
avg_grade_per_student = np.mean(grades, axis=1)
print("\nAverage grade per student:\n", avg_grade_per_student)

# b) Task: Compute average grade per subject (column-wise)
avg_grade_per_subject = np.mean(grades, axis=0)
print("\nAverage grade per subject (Math, Science, English, History):\n", avg_grade_per_subject)

# c) Task: Find the highest-scoring student in each subject
# Returns the row indices (student numbers)
top_scorers_per_subject = np.argmax(grades, axis=0)
print("\nHighest-scoring student index in each subject:\n", top_scorers_per_subject)

# d) Task: Determine pass/fail status per student (pass if average ≥ 60)
pass_fail_status = np.where(avg_grade_per_student >= 60, "Pass", "Fail")
print("\nPass/Fail status per student:\n", pass_fail_status)

# e) Task: Compute the class median grade (of all grades together)
class_median = np.median(grades)
print("\nClass median grade:\n", class_median)
