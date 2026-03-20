#batch7_no10
user_string = input("Enter the main string: ")
target = input("Enter the target to find: ")

target_length = len(target)
found_index = -1

if target_length > 0:
    # Loop backwards through the string
    for i in range(len(user_string) - target_length, -1, -1):
        if user_string[i:i + target_length] == target:
            found_index = i
            break

if found_index != -1:
    print(f"Output: Found at index {found_index}")
else:
    print("Output: Target not found (ValueError)")