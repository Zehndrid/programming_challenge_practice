#batch5_no1
user_fullname = input("Enter your full name with spaces at the beginning: ")

# Use lstrip() or leftstrip() to remove spaces only from the left side
clean_fullname = user_fullname.lstrip()

print(f"Output: {clean_fullname}")