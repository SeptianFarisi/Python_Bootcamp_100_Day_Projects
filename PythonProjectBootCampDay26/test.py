# double_number = [n * 2 for n in range(1,5)]
# print(double_number)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# caps_name = [name.upper() for name in names if len(name) > 5]
# print(caps_name)

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {student:random.randint(1,100) for student in names}
# print(student_score)
passed_student = {student:score for (student, score) in student_score.items() if score >= 60}
print(passed_student)