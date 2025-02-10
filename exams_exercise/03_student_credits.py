def students_credits(*args):

    # course_percent = int((data[3])/int(data[2]) * 100
    # gained_points = int(data[1])/100 * course_percent
    points = 0
    courses = {}
    result = []
    for data in args:
        course,credits,max_points,poitns = data.split("-")
        course_percent = int(poitns)/int(max_points) * 100
        gained_points_on_course = (int(credits)/100) * course_percent
        if course in courses:
            continue
        courses[course] = gained_points_on_course
        points += gained_points_on_course

    if points >= 240:
        result.append(f"Diyan gets a diploma with {points:.1f} credits.\n")
    else:
        result.append(f"Diyan needs {(240 - points):.1f} credits more for a diploma.\n")
    sorted_course = dict(sorted(courses.items(),key=lambda x: -x[1]))
    for course,points in sorted_course.items():
        result.append(f"{course} - {points:.1f}\n")
    return "".join(result)

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
