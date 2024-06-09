def get_top_students(**students_scores):
    top_students = []
    for name, marks in students_scores.items():
        if marks >= 90:
            top_students.append(name)
    return top_students

print(get_top_students(Tom= 90,Steve = 99,Paul=87,Kevin=43))
