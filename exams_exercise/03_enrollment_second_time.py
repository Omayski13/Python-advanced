def gather_credits(needed_credits,*args):
    points = 0
    courses = []
    result = []
    for course,credit in args:
        if needed_credits <= points:
            break
        if course in courses:
            continue
        courses.append(course)
        points += int(credit)

    if points >= int(needed_credits):
        result.append(f"Enrollment finished! Maximum credits: {points}.\n")
        result.append(f"Courses: {', '.join(courses)}")
        return f"""Enrollment finished! Maximum credits: {points}.
Courses: {', '.join(sorted(courses))}"""

    result.append(f"You need to enroll in more courses! You have to gather {needed_credits - points} credits more.")
    return "".join(result)

print(gather_credits(
    80,
    ("Basics", 27),
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
