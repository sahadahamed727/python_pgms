# Student Performance Analysis System

# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)


# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to find highest mark
def find_highest(marks):
    return max(marks)


# Function to find lowest mark
def find_lowest(marks):
    return min(marks)


# Function to determine grade
def find_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Get number of students
n = int(input("Enter the number of students: "))

students = []

# Accept student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = float(input("Enter mark for subject " + str(j + 1) + ": "))
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = find_grade(average)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    }

    students.append(student)


# Sort students according to total marks using lambda
students.sort(key=lambda x: x["total"], reverse=True)


# Display results
print("\n-------- Student Performance Analysis --------")

for student in students:
    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"])
    print("Average:", round(student["average"], 2))
    print("Highest:", student["highest"])
    print("Lowest:", student["lowest"])
    print("Grade:", student["grade"])