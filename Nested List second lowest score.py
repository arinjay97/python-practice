students = []
marks = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    marks.append(score)
marks.sort()
students.sort()
m = list(set(marks))
m.sort()
print(students)
print(m)

for a, b in students:
    if b == m[1]:
        print(a)