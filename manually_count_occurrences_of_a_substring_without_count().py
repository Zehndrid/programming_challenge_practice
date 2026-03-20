#batch7_no8
user_string = input("Enter the main string: ")
target = input("Enter the string to count: ")

target_length = len(target)
occurrences = 0

if target_length > 0:
    # Loop through the string, stopping early enough so we don't read past the end
    for i in range(len(user_string) - target_length + 1):
        # Take a slice of the string exactly the size of our target and compare
        if user_string[i:i + target_length] == target:
            occurrences += 1

print(f"Output: {occurrences}")