###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char == 'z':
         char == 'a'
    if char == 'Z':
         char == 'A'
    if char == " ":
         char == " "
    else:
              
        ord(char)
    
        # add one to the character's code
        char = ord(char)

        # replace new character code with its
        char = char + 1

         # corresponding character (use chr())
        char = chr(char)
        
         # add encrypted character to encrypted text
    encrypted_text = encrypted_text + char    

print(f'{plain_text}')
print(f'{encrypted_text}')