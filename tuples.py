#Name :- Mayuri Pawar 
#Branch :- Computer Engineering
# Tuples example
employees = [
    ("Amit", "HR", 50000),
    ("Neha", "Engineering", 70000),
    ("Ravi", "HR", 60000),
    ("Priya", "Engineering", 65000),
    ("Karan", "Sales", 55000)
]

sorted_employees = sorted(employees, key=lambda x: (x[1], -x[2]))


for emp in sorted_employees:
    print(emp)

