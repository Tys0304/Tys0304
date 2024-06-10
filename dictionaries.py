student = {
    "name": "Alice",
    "age": int(20),
    "major": "Computer Science",
    "grades": {
        "math": 95,
        "english": 88,
        "history": 92
    }
}

student_name = student["name"]
student_age = student["age"]

student["age"] = 21
student["grades"]["math"] = 97

student["gender"] = "Female"

has_major = "major" in student
has_height = "height" in student

keys = student.keys()
values = student.values()

print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

del student["grades"]

print("\nStudent Information after removing 'grades':")
for key, value in student.items():
    print(f"{key}: {value}")