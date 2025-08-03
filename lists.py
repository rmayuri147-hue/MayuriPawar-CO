#Name :- Mayuri Pawar 
#Branch :- Computer
# List Example
students = [
    ("Amit", 10, 88),
    ("Neha", 9, 92),
    ("Ravi", 10, 95),
    ("Priya", 9, 85),
]

sorted_students = sorted(students, key=lambda x: (x[1], -x[2]))

for s in sorted_students:
    print(s)

