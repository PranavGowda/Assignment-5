
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

name = input("Enter the student's name: ")

if name in students:
    print("Marks of", name, "are:", students[name])
else:
    print("Student not found in the record.")
