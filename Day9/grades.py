student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 91,
    "Draco": 74,
    "Neville": 62,
}

stud_grades = {}

for key in student_scores:
    if student_scores[key] <= 70:
        stud_grades[key] = "Fail"
    elif student_scores[key] > 70 and student_scores[key] < 81:
        stud_grades[key] = "Acceptable"

    elif student_scores[key] > 80 and student_scores[key] < 91:
        stud_grades[key] = "Exceeds Expectations"
    else:
        stud_grades[key] = "Outstanding"

print(stud_grades)
