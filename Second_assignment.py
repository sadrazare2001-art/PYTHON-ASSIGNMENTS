students_list = []
number_students = int(input("How many students are there? "))

total = 0

for i in range(number_students):
    name = input("Please enter the student's name: ")
    grade = int(input("Please enter the grade: "))
    students_list.append({"name": name, "grade": grade})
    total += grade  # Keep running total

print("\nStudents and their grades:")
for student in students_list:
    print(f"{student['name']} -> {student['grade']}")

# Average
average = total / number_students

# Highest & lowest grade
highest = max(students_list, key=lambda x: x["grade"])
lowest = min(students_list, key=lambda x: x["grade"])

print("\n📊 Summary:")
print("Total of all grades:", total)
print("Average grade:", average)
print(f"Highest grade: {highest['name']} with {highest['grade']}")
print(f"Lowest grade: {lowest['name']} with {lowest['grade']}")
