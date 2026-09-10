Grades = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 78,
    "Ayesha": 95,
    "Hamza": 88
}

total = 0

for score in Grades.values():
    total += score

average = total / len(Grades)

print("=======Student Grade Book======")
print("Class Average", average)

highest_score = max(Grades.values())
lowest_score = min(Grades.values())

top_student = max(Grades, key=Grades.get)
bottom_student = min(Grades, key=Grades.get)

print("Top Scorer:", top_student, "-", highest_score)
print("bottom scorer:", bottom_student, "-", lowest_score)

student_name = input("\nEnter a student name to search:")
score = Grades.get(student_name)

if score is not None:
    print(student_name, "scored", score)
else:
    print("sorry, student not found")