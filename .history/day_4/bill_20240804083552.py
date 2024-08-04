# wap which will select a random name from a list of names. The person selectsed will have to pay for everybody's food bill. 
import
names_string = input("Give me everybody's names, seperated bt a comma.")
names = names_string.split(",") # we can directly convert it into a list by seperating out the commas using str.split(',') 

print(names)
