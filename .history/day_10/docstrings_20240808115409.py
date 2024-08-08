length= len("formatted_name")

def format_name(f_name, l_name):
    """
    Doctstring
    
    Take a first and last name 
    and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
      return "You idn't provide valid inputs."  
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    

