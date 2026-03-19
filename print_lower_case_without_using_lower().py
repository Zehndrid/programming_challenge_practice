#batch6_no3
user_string = input("Enter a string: ")
result_string = ""

for char in user_string:
    #check if the character is an uppercase letter (A-Z)
    if 'A' <= char <= 'Z':
        #ord() gets the ASCII number (e.g., 'A' is 65). Add 32 to get lowercase ('a' is 97). 
        #chr() turns that new number back into a letter.
        lower_char = chr(ord(char) + 32)
        result_string += lower_char
    else:
        #if it's already lowercase, a number, or a space, leave it alone
        result_string += char

print(f"Output: {result_string}")