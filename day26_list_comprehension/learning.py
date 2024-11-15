'''LIST COMPREHENSIONS'''
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# num_range = range(1,5)
# print(f"Normal Range: {num_range}")
# doubled_range = [n*2 for n in num_range]
# print(f"Doubled Range: {doubled_range}")

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name)<5]
# print(f"Short names: {short_names}")
# long_names = [name.upper() for name in names if len(name)>=5]
# print(f"Long names: {long_names}")

'''DICTIONNARY COMPREHENSIONS'''
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {name:random.randint(1,100) for name in names}
# print(students_scores)
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

'''LOOP THROUGH A PANDAS DATAFRAME'''
import pandas
students_dict = {
    'student': ['Alex', 'Beth', 'Caroline'],
    'score': [56, 76, 98]
}
student_dataframe = pandas.DataFrame(students_dict)
print(student_dataframe)
# Loop throuhg rows of a DF
for (index, row) in student_dataframe.iterrows():
    print(row.score)