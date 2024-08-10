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
if year >1980 and year < 1994:
    print("You are a millenial")
elif year >= 1994:
    print("You are  gE")