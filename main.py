students = {}

for i in range(1, 4):
    student_number = input(f"Enter student number for classmate {i}: ")
    first_name = input(f"Enter first name for classmate {i}: ")
    students[student_number] = first_name

print("\nOriginal Student List:")
for student_number, first_name in students.items():
    print(f"Student Number: {student_number}, First Name: {first_name}")

if len(students) >= 3:
    third_key = list(students.keys())[2]
    students.pop(third_key)
else:
    print("Not enough entries to remove the third one.")

my_student_number = input("\nEnter your student number: ")
my_first_name = input("Enter your first name: ")
students[my_student_number] = my_first_name

print("\nUpdated Student List:")
for student_number, first_name in students.items():
    print(f"Student Number: {student_number}, First Name: {first_name}")
