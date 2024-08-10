############ DEBUGGING ###########

# Describe Problem
def my_function():
    # for i in range(1, 20):         ❌
    for i in range (1, 21):        # ✅
        if i == 20:
            print("You got it")
my_function()


# Reproducing the Bug
from random import randint
dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣" ]
# dice_num = randint(1, 6)                                ❌                   
dice_num = randint(0, 5)                                # ✅
print(dice_imgs[dice_num])


# Play Computer
year = int(input("What's you year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial")
elif year >= 1994:
    print("You are Gen Z. ")
    

# Fix the Errors and watching red underline
# age = input("How old are you?")                       ❌                        
age = int(input("How old are you?"))                  # ✅      
if age > 18:
    print("You can drive at age {age}.")


#Print is your friend
pages = 0
word_per_page = 0
pages = int(input("Number of page: "))
# word_per_page == int(input("Number of words per page: "))       ❌
word_per_page = int(input("Number of words per page: "))        # ✅ 
total_words = pages * word_per_page
print(f"pages = {pages}")   # added
print(f"word_per_page = {word_per_page}")
print("Total words: ", total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
        print(b_list)