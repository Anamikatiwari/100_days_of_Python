# function with output

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"
# formated_string = format_name("AnAmIkA", "TIWARI")
# print(formated_string)
print(format_name("AnAmIkA", "TIWARI"))

output= len("Anamika")

#multiple return value
def format_name(f_name, l_name):
    # if f_name == "" or l_name == "":
        
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
print(format_name(input))
