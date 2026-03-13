#batch5_no10
#input the full name of the user
user_fullname = input("Enter your full name: ")
#using lower() and replace() to print the input in snake case
snake_case_fullname = user_fullname.lower().replace(" ", "_")
print(f"Output: {snake_case_fullname}")
