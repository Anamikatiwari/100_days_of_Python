# wap that calculate the sum of all the even numbers from 1 to 100, including 1 and 100. 

total = 0
for number in range(2, 101, 2):
    total += number
    print(total)  # Output: 2550
    
    
# or
total2= 0
for number in range(1, 101)