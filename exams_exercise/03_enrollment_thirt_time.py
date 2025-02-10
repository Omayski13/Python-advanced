def gather_credits(needed_credits, *args):
    courses = []
    result = []
    points = 0
    for data in args:
        course = data[0]
        course_points = int(data[1])
        if course in courses:
            continue
        if points >= needed_credits:
            break
        courses.append(course)
        points += course_points
    if points >= needed_credits:
        result.append(f"Enrollment finished! Maximum credits: {points}.\n")
        result.append(f"Courses: {', '.join(sorted(courses))}")
        return "".join(result)
    else:
        result.append(f"You need to enroll in more courses! You have to gather {needed_credits - points} credits more.")
    return "".join(result)




print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Basics", 32),
    ("Fundamentals", 27),
))


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

