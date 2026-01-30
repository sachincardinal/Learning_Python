# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show a message if not found
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found.")
