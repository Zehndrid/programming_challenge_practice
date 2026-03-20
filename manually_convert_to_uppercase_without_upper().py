#batch7_no3
user_string = input("Enter a string: ")
result_string = ""

for char in user_string:
    # Check if the character is a lowercase letter (a-z)
    if 'a' <= char <= 'z':
        # ord() gets the ASCII number (e.g., 'a' is 97). Subtract 32 to get uppercase ('A' is 65).
        upper_char = chr(ord(char) - 32)
        result_string += upper_char
    else:
        # If it's already uppercase, a number, or a space, leave it alone
        result_string += char

print(f"Output: {result_string}")