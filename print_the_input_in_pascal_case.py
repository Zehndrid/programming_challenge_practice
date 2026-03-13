#batch5_no9
#input the full name of the user
user_fullname = input("Enter your full name: ")
#using title() to print the input in Pascal Case
pascal_case_fullname = user_fullname.title().replace(" ", "")
print(f"Output: {pascal_case_fullname}")