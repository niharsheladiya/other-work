# Welcome to the student data analysis program


import datetime
import time
import math
import random
import uuid
import numpy as np




# Standard Python Modules (datetime, time, random, uuid, math)

current_date_time = datetime.datetime.now()
print(f"Current Date and Time: {current_date_time}")

system_time = time.time()
print(f"System Timestamp: {system_time}")

student_id = uuid.uuid4()
print(f"Unique Student ID: {student_id}")

student_age = random.randint(18, 25)
print(f"Student Age: {student_age}")

attendance_score = 75
sqrt_attendance = math.sqrt(attendance_score)
print(f"Square root of attendance score: {sqrt_attendance:.2f}")






# Lists and Higher-Order Functions (sorted, map, filter)

marks = [45, 82, 38, 91, 55, 64]
print(f"\nOriginal Marks List: {marks}")

sorted_marks = sorted(marks)
print(f"Sorted Marks: {sorted_marks}")

squared_marks = list(map(lambda x: x**2, marks))
print(f"Squared Marks: {squared_marks}")

passed_marks = list(filter(lambda x: x > 50, marks))
print(f"Filtered Marks: {passed_marks}")








# NumPy Array Operations (Creation, Indexing, Slicing, Math, Reshaping, Masking)

np_marks = np.array(marks)
print(f"\nNumPy Array: {np_marks}")

first_mark = np_marks[0]
print(f"First mark: {first_mark}")

sliced_marks = np_marks[1:4]
print(f"Sliced marks: {sliced_marks}")

grace_marks = np_marks + 5
print(f"Marks with 5 grace marks: {grace_marks}")

reshaped_marks = np_marks.reshape(2, 3)
print("Reshaped Array (2x3):")
print(reshaped_marks)

mask = np_marks > 60
print(f"Boolean Mask (>60): {mask}")

high_marks = np_marks[mask]
print(f"Marks greater than 60: {high_marks}")









# NumPy Statistical Functions

total_marks = np.sum(np_marks)
average_marks = np.mean(np_marks)
min_mark = np.min(np_marks)
max_mark = np.max(np_marks)

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Minimum Mark: {min_mark}")
print(f"Maximum Mark: {max_mark}")









