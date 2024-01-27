# Question 1:
# Create an empty dictionary named student_info. Add the following key-value pairs to the dictionary:

# 'name': 'John'
# 'age': 25
# 'grade': 'A'

# Empty dictonary
student_info = {}
# Adding values in Empty dictonary
student_info['name'] = 'Jhon'
student_info['age'] = 25
student_info['grade'] = 'A'
print(student_info)

# Question 2:
# Given the dictionary student_info from Question 1, update John's age to 26.
# student_info['age] = 26
new = {'age': 26}
student_info.update(new)
print(student_info)


# Question 3:
# Create a dictionary named course_grades with the following key-value pairs:

# 'math': 'B'
# 'english': 'A'
# 'history': 'C'
# Combine the student_info and course_grades dictionaries into a new dictionary named final_report.
final_report = {}
course_grades = {'math': 'B', 'english': 'A', 'history': 'C'}
student_info.update(course_grades)
final_report.update(student_info)
print(final_report)
# ALSO
# final_report = {**student_info, **course_grades}
# print(final_report)

# Question 4:
# Using the final_report dictionary from Question 3, remove the entry for 'history'.
# del final_report('history')

final_report.popitem()
print(final_report)

# Question 5:
# Check if the key 'grade' is present in the final_report dictionary
if 'grade' in final_report.keys() :
    print(f"key 'grade' is present")
else:
    print("Key 'grade' is not present")