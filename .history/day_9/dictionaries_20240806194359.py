#dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over again.",
    # "Loop": "The action of doing something over and over again."
    }

#Retrieving item from dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary. 
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary. 
empty_disctionary = {}

#Wipe an existing dictionary. 
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary. 
programming_dictionary["Bug"]