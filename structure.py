name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course: ")
branch = input("Enter branch: ")

student = {
    "Name": name,
    "Age": age,
    "Course": course,
    "Branch": branch
}

print("\nStudent Information")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])
print("Branch:", student["Branch"])
