def gather_credits(needed_credits,*args):
    result = []
    enrolled_courses = []
    enrolled_credits = 0
    for course,course_credit in args:
        if course in enrolled_courses:
            continue
        enrolled_courses.append(course)
        enrolled_credits += course_credit
        if enrolled_credits >= needed_credits:
            result.append(f"Enrollment finished! Maximum credits: {enrolled_credits}.\n")
            sorted_result = sorted(enrolled_courses, key=lambda x: x)
            result.append(f"Courses: {', '.join(sorted_result)}")
            break
    else:
        result.append(f"You need to enroll in more courses! You have to gather {needed_credits - enrolled_credits} credits more.")


    return "".join(result)


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

