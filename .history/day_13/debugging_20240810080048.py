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
dice_num = randint(1, 6)
