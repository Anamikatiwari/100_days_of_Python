# wap that calculates the average student height for a list of heights. 

student_heights = input("Input a list of stuent heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# print(sum(student_heights))
total_height = 0
for height in student_heights:
    total_height += height
print


number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)