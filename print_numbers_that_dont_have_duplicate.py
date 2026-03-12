#batch3_no1
#create an empty list to store the numbers
user_numbers = []

print("Please enter 10 numbers:")

#loop 10 times to collect the inputs
for i in range(10):
    current_number = int(input(f"Enter number {i + 1}: "))
    #add the newly entered number to the end of our list
    user_numbers.append(current_number)

print("\nThese are the numbers that have no duplicates:")

#loop through the filled list
for number in user_numbers:
    #.count() checks if the numbers is only counted once in the list.
    if user_numbers.count(number) == 1:
        print(number)