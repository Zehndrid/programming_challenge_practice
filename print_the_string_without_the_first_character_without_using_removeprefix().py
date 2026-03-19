#batch6_no2
user_string = input("Enter the main string: ")
prefix = input("Enter the prefix to remove: ")

prefix_length = len(prefix)

# Check if the very beginning of the string matches the prefix perfectly
if user_string[:prefix_length] == prefix:
    # If it matches, slice the string starting from AFTER the prefix
    result = user_string[prefix_length:]
else:
    # If it doesn't match, nothing changes
    result = user_string

print(f"Output: {result}")