"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76





1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

2. Write a for loop to calculate the average score of the students. Print the average score.

3. Write a for loop to assign grades based on the following criteria:
Score >= 90: Grade A
Score >= 80 and < 90: Grade B
Score >= 70 and < 80: Grade C
Score < 70: Grade D
Store these grades in a new dictionary called student_grades.

4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.
"""

student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76
}
# 1
for student, score in student_scores.items():
    print("Student:", student, ", Score:", score)
# 2
total_score = 0
for score in student_scores.values():
    total_score += score
average_score = total_score / len(student_scores)
print("Average Score:", average_score)

# 3
student_grades = {}
for student, score in student_scores.items():
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    student_grades[student] = grade
print("Student Grades:", student_grades)

# 4
for student in student_scores:
    student_scores[student] += 5
print("Updated Student Scores:", student_scores)

"""
Create a dictionary named employee_data with the following key-value pairs:
"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.


# """

employee_data = {
    "John": 55000,
    "Emma": 60000,
    "Harry": 70000,
    "Sophia": 65000,
    "Mike": 48000
}

# 1.
for employee, salary in employee_data.items():
    if salary > 60000:
        print("Employee earning more than $60,000:", employee)

# 2. 
for employee in employee_data:
    employee_data[employee] *= 1.10
print("Updated Employee Salaries:", employee_data)


# # Create a dictionary named library_books with the following key-value pairs:
# "The Great Gatsby": 4
# "1984": 6
# "To Kill a Mockingbird": 3
# "The Catcher in the Rye": 5
# "Moby Dick": 2

# 1. Write a for loop to add 2 more copies to each book. Update the dictionary accordingly.
# 2. Write a for loop to calculate the total number of books in the library. Print the total count.
# """

library_books = {
    "The Great Gatsby": 4,
    "1984": 6,
    "To Kill a Mockingbird": 3,
    "The Catcher in the Rye": 5,
    "Moby Dick": 2
}

# 1.
for book in library_books:
    library_books[book] += 2
print("Updated Library Books:", library_books)

# 2.
total_books = 0
for copies in library_books.values():
    total_books += copies
print("Total number of books:", total_books)

"""
consider the list of dicts
book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]
Write a for loop to assign one more detail "stock" based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e book_list.
"""

book_list = [
    {"name": "The Great Gatsby", "quantity": 4},
    {"name": "1984", "quantity": 6},
    {"name": "To Kill a Mockingbird", "quantity": 3},
    {"name": "Moby Dick", "quantity": 2}
]

# 
for book in book_list:
    if book["quantity"] >= 5:
        book["stock"] = "Popular"
    elif book["quantity"] >= 3:
        book["stock"] = "Available"
    else:
        book["stock"] = "Limited"
print("Updated Book List:", book_list)

"""
Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}


1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. Add new Student and its subject, score and class in same dict i.e students
7. add new subject and its score in John
"""


# Create the students dictionary
students = {
    "Alice": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [85, 90, 78],
        "Class": 10
    },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

# 1. 
print("Alice's English Score:", students["Alice"]["Scores"][2])

# 2. 
print("Bob's Class:", students["Bob"]["Class"])

# 3. 
print("Charlie's Math Score:", students["Charlie"]["Scores"][0])

# 4. 
diana_scores = students["Diana"]["Scores"]
diana_avg_score = sum(diana_scores) / len(diana_scores)
print("Diana's Average Score:", diana_avg_score)

# 5. 
john_subjects = students["John"]["Subjects"]
john_scores = students["John"]["Scores"]
for subject, score in zip(john_subjects, john_scores):
    print("Student: John, Subject:", subject, ", Score:", score)

# 6. 
students["Emma"] = {
    "Subjects": ["Math", "Science", "History"],
    "Scores": [90, 85, 88],
    "Class": 10
}
print("Updated Students:", students)

# 7. 
students["John"]["Subjects"].append("History")
students["John"]["Scores"].append(70)
print("John's Updated Information:", students["John"])


"""
Givent the list of students
students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
]

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. display which class obtained the higher marks
7. display the student name that obtain high marks in subject Math in class 10
8. Add new Student and its subject, score and class in same dict i.e students
"""

# Create the students list
students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
]

# 1. 
for student in students:
    if student["name"] == "Alice":
        print("Alice's English Score:", student["scores"][2])

# 2. 
for student in students:
    if student["name"] == "Bob":
        print("Bob's Class:", student["Class"])

# 3. 
for student in students:
    if student["name"] == "Charlie":
        print("Charlie's Math Score:", student["scores"][0])

# 4. 
for student in students:
    if student["name"] == "Diana":
        avg_score = sum(student["scores"]) / len(student["scores"])
        print("Diana's Average Score:", avg_score)

# 5. 
students.append({
    "name": "John",
    "subjects": ["Math", "Science", "English"],
    "scores": [50, 60, 60],
    "Class": 11
})

for student in students:
    if student["name"] == "John":
        for subject, score in zip(student["subjects"], student["scores"]):
            print("Student: John, Subject:", subject, ", Score:", score)

# 6. 
class_scores = {}
for student in students:
    class_id = student["Class"]
    total_score = sum(student["scores"])
    if class_id in class_scores:
        class_scores[class_id] += total_score
    else:
        class_scores[class_id] = total_score

highest_class = max(class_scores, key=class_scores.get)
print("Class with higher marks:", highest_class)

# 7. 
highest_math_score = 0
top_student = ""
for student in students:
    if student["Class"] == 10 and student["scores"][0] > highest_math_score:
        highest_math_score = student["scores"][0]
        top_student = student["name"]

print("Student with highest marks in Math in class 10:", top_student)

# 8. 
students.append({
    "name": "Emma",
    "subjects": ["Math", "Science", "History"],
    "scores": [90, 85, 88],
    "Class": 10
})
print("Updated Students:", students)
