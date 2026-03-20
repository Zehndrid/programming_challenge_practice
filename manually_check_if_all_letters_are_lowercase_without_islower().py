#batch7_no4
user_string = input("Enter a string: ")

is_all_lower = True
has_a_letter = False

for char in user_string:
    # If we find even a single uppercase letter, the test fails
    if 'A' <= char <= 'Z':
        is_all_lower = False
        break
    # We must also prove that there is at least ONE lowercase letter
    elif 'a' <= char <= 'z':
        has_a_letter = True

# If there were no uppercase letters, BUT there were no letters at all (like "123!"), it's False
if not has_a_letter:
    is_all_lower = False

print(f"Output: {is_all_lower}")