# wap that adds the digits in a 2 digit number
two_digit_number= input("Type a two digit number")

#check the data type of two_digit_number
print(type(two_digit_number))

#get the first and second digit using subscripting
first_digit= two_digit_number[0]
second_digit= two_digit_number[1]

#Add the two digits together and 
result= int(first_digit) + int(second_digit)
print(result)