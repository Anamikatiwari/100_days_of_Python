# wap that works out whether if a given number is an odd or even number

number = int(input("which number do you want to c"))

7 % 2 #output=1
# 7 % 2 = 1 because 7 divided by 2 leaves a remainder of 1

if number % 2 == 0:
    print("This is a even number")
else:
    print("This is an odd number")