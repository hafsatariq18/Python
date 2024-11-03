# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.

N, X = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(X)]

student_marks = zip(*marks)

for student in student_marks:
    average = sum(student) / X
    print(average)