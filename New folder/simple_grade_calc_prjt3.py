def assign_grades(scores):
    # Use map with a lambda function to assign grades
    grades = list(map(lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F', scores))
    return grades

def main():
    scores = [95, 82, 67, 54, 88, 76, 90]
    print("Student Scores:", scores)
    print("Assigned Grades:", assign_grades(scores))

main()
