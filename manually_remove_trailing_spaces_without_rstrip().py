#batch7_no1
user_string = input("Enter a string with spaces at the end: ")
end_index = len(user_string)

# Loop backwards through the string starting from the very last character
for i in range(len(user_string) - 1, -1, -1):
    if user_string[i] != " ":
        # Once we find a real character, mark the index right AFTER it
        end_index = i + 1
        break
    # If we make it all the way to index 0 and it's still a space, the string is empty
    if i == 0 and user_string[i] == " ":
        end_index = 0

# Slice the string from the beginning to our calculated end_index
clean_string = user_string[:end_index]

print(f"Output: '{clean_string}'")