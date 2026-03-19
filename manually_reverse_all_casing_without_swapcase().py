#batch6_no7
user_string = input("Enter a string in mixed casing: ")
result_string = ""

for char in user_string:
    if 'A' <= char <= 'Z':
        # If it is uppercase, add 32 to make it lowercase
        result_string += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        # If it is lowercase, subtract 32 to make it uppercase
        result_string += chr(ord(char) - 32)
    else:
        result_string += char

print(f"Output: {result_string}")