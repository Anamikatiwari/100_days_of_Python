# wap which will select a random name from a list of names. The person selectsed will have to pay for everybody's food bill. 
import random
names_string = input("Give me everybody's names, seperated bt a comma.")
names = names_string.split(",") # we can directly convert it into a list by seperating out the commas using str.split(',') 

# get  the total number of items in list
"""num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "is going to buy the meal today.")

"""