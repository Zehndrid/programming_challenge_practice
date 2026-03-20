#batch7_no5
user_string = input("Enter the main string: ")
prefix = input("Enter the prefix to check: ")

prefix_length = len(prefix)

# Grab the slice from the very beginning of the string
if len(user_string) >= prefix_length and user_string[:prefix_length] == prefix:
    print("Output: True")
else:
    print("Output: False")