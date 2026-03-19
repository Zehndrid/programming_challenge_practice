#batch6_no4
user_string = input("Enter a string: ")

is_all_upper = True
has_a_letter = False

for char in user_string:
    # If we find even a single lowercase letter, the test fails
    if 'a' <= char <= 'z':
        is_all_upper = False
        break
    # We must also prove that there is at least ONE uppercase letter in the whole string
    elif 'A' <= char <= 'Z':
        has_a_letter = True

# If there were no lowercase letters, BUT there were no letters at all (like "123!"), it's False
if not has_a_letter:
    is_all_upper = False

print(f"Output: {is_all_upper}")