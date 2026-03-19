#batch6_no9
user_string = input("Enter a string: ")

if len(user_string) > 0:
    first_char = user_string[0]
    rest_of_string = ""
    
    # Capitalize the first character manually using ASCII math
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
        
    # Force the rest of the string into lowercase manually
    for char in user_string[1:]:
        if 'A' <= char <= 'Z':
            rest_of_string += chr(ord(char) + 32)
        else:
            rest_of_string += char
            
    result = first_char + rest_of_string
else:
    result = ""

print(f"Output: {result}")