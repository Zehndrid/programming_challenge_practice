#batch4_no1
#create an empty list to store the numbers
user_numbers = []
already_printed = []

print("Please enter 10 numbers:")

#loop 10 times to collect the inputs
for i in range(10):
    current_number = int(input(f"Enter number {i + 1}: "))
    #add the newly entered number to the end of our list
    user_numbers.append(current_number)

print("\nThese are the numbers that had duplicates:")

#loop through the filled list
for number in user_numbers:
    #.count() checks if the number is counted more than once in the list.
    if user_numbers.count(number) > 1 and number not in already_printed:
        already_printed.append(number)
        print(number)