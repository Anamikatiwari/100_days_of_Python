# wap that calculates the highest score from a list of scores. 
student_scores = input("Input a list of student")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
    

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("The highest score in a class is: {highest_score}")