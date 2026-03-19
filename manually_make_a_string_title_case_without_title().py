#batch6_no10
user_string = input("Enter a string: ")
result_string = ""

# A flag to track if we are at the start of a brand new word
is_new_word = True

for char in user_string:
    if char == " ":
        # If we hit a space, the NEXT letter must be a new word
        result_string += char
        is_new_word = True
    elif is_new_word:
        # If it's a new word, capitalize the letter
        if 'a' <= char <= 'z':
            result_string += chr(ord(char) - 32)
        else:
            result_string += char
        # Turn off the flag so the next letters stay lowercase
        is_new_word = False
    else:
        # If it's the middle of a word, force it to be lowercase
        if 'A' <= char <= 'Z':
            result_string += chr(ord(char) + 32)
        else:
            result_string += char

print(f"Output: {result_string}")