#batch6_no5
user_string = input("Enter the main string: ")
suffix = input("Enter the suffix to check: ")

suffix_length = len(suffix)

# Grab the slice from the very end of the string counting backwards
# Example: if suffix is 3 letters long, user_string[-3:] gets the last 3 letters
if len(user_string) >= suffix_length and user_string[-suffix_length:] == suffix:
    print("Output: True")
else:
    print("Output: False")