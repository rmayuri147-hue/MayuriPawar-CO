#Name :- Mayuri Pawar 
#Branch :- Computer 
#Sets Example

students = [
    {"name": "Amit", "class": 10, "marks": 88},
    {"name": "Neha", "class": 9, "marks": 92},
    {"name": "Ravi", "class": 10, "marks": 95},
    {"name": "Priya", "class": 9, "marks": 85},
    {"name": "Karan", "class": 8, "marks": 90},
]

sorted_students = sorted(students, key=lambda x: (x["class"], -x["marks"]))

#Result For Set
for student in sorted_students:
    print(student)
