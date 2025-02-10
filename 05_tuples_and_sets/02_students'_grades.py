students = int(input())
grades = {}

for n in range(students):
    name, grade = input().split()
    if name not in grades:
        grades[name] = []
    grades[name].append(float(grade))

for student_name, grades in grades.items():
    # print(name)
    # print(grades[name])
    # print(sum((grades)[name]))
    # # print(len(grades)[name])
    formatted_grades = " ".join([f"{grade:.2f}" for grade in grades])
    print(f"{student_name} -> {formatted_grades} (avg: {sum(grades)/len(grades):.2f})")