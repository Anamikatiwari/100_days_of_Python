#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88  
 
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88                                             

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
    end_text


#TODO-2- Call the caesar() function, passing over the 'text', 'shift', and 'direction' values. 

#vdo- 086