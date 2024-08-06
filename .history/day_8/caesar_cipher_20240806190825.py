                                      
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#encrypt

#TODO-1- Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The encoded text is {cipher_text}")
    
    #TODO-2- Inside the 'encrypt' function, shift each letter of the 'text' forward in the alphabet by the shift amount and print the encrypted text. 
    
    
#TODO-3- Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message
encrypt(plain_text=text, shift_amount=shift)

#---------------------------------------------------------------------------------------

#decrypt

#TODO-1- Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")

   #TODO-2- Inside the 'decrypt' function, shift each letter of the 'text' backward in the alphabet by the shift amount and print the decrypted text.

#TODO-3- Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message 
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Reorganizing code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1- Combining the encrypt() and decrypt() functions into a single  function called caesar(). 
def caesar(start_text, shift_amount, cipher_direction):
    end_text =""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
            new_position = position + shift_amount
        end_text += alphabet[new_position]
        print(f"The {cipher_direction}d is {end_text}")
           
#TODO-2- Call the caesar() function, passing over the 'text', 'shift', and 'direction' values. 
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#user experience improvement

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text =""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3- What happen if the user enter a number/symbol/space? 
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
        
    print(f"Here's the {cipher_direction}d result: {end_text}")
   
   
#TODO-1- Import and print the logo from art.py when the program starts. 
from art import logo
print(logo)

#TODO-4- Can you figure out a way to ask the user if they want to restart  the cipher program? 
#e.g; Type 'Yes' if you want to go again. Otherwise type 'No'. 
#If they type 'Yes' then ask them for the direction/text/shift again and call the caesar() function again? 
#Hint: Try creating a new function that calls itself if they type 'Yes'

direction = input("Type 'encode' to encript, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-2- What if the user enters a shift that is greater than number of letters in the alphabet?
#Try running the program and entering a shift number of 45. 
#Hint: Think about how you can use the modulus(%)

shift = shift % 26
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)