#batch6_no1
user_string = input("Enter a string with spaces at the beginning: ")
start_index = 0

#loop through the string until we find the first character that IS NOT a space
for i in range(len(user_string)):
    if user_string[i] != " ":
        start_index = i
        break

#slice the string from that first real character all the way to the end
clean_string = user_string[start_index:]

print(f"Output: {clean_string}")