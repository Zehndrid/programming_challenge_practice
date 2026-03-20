#batch7_no1
user_string = input("Enter the main string: ")
suffix = input("Enter the suffix to remove: ")

suffix_length = len(suffix)

# Check if the very end of the string matches the suffix perfectly
if suffix_length > 0 and len(user_string) >= suffix_length and user_string[-suffix_length:] == suffix:
    # If it matches, slice the string to exclude the suffix
    result = user_string[:-suffix_length]
else:
    # If it doesn't match, keep the original string
    result = user_string

print(f"Output: {result}")