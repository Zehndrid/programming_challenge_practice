#batch6_no6
user_string = input("Enter a string: ")
target_length = int(input("Enter total character length: "))

# Calculate how many spaces we are missing
spaces_needed = target_length - len(user_string)

if spaces_needed > 0:
    # Multiply the space character by the number needed and add it to the end
    result = user_string + (" " * spaces_needed)
else:
    result = user_string

print(f"Output: '{result}'")