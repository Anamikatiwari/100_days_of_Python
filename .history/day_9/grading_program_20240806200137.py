# wap that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked. 

student_scores = {
    "Harry": 81,
    "Ron": 78, 
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

#TODO-1- Create an empty dictionary called student_grades. 
student_grades = {}

#TODO-2- Write your code below to add the grades to student_grades
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exc"
print(student_grades)