student_scores = [12,24,5,2,6,7,10,24,25,30,27,100]
max_score = 0
# for i in range(len(student_scores)-1):
#     j = i + 1
#     if student_scores[i] > student_scores[j]:
#         max_value = student_scores[i]
#     else:
#         max_value = student_scores[j]
# print(max_value)
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)