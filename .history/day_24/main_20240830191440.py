# file = open("my_file.txt")    # open file
# contents = file.read()        # read file
# print(contents)               # print file
# file.close()                  # close the file



# with open("my_file.txt") as file: 
#     contents = file.read()        
#     print(contents)               
   
   
   
# rename file
# with open("my_file.txt", mode="w") as file: 
#    file.write("New Text.")


#append
# with open("my_file.txt", mode="a") as file: 
#    file.write("\nNew Text.")

# if file doesn't exist, it create 
with open("new_file.txt", mode="w") as file: 
   file.write("New Text.")
   
   
# video- 220 
# In day 