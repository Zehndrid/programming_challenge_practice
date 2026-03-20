#batch7_no7
user_string = input("Enter a number string: ")
target_length = int(input("Enter total character length: "))

zeros_needed = target_length - len(user_string)

if zeros_needed > 0:
    # Multiply the "0" character and add it to the BEGINNING of the string
    result = ("0" * zeros_needed) + user_string
else:
    result = user_string

print(f"Output: '{result}'")