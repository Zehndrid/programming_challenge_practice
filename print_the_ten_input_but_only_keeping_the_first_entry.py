#batch3_no2
unique_numbers = []

print("Please enter 10 numbers:")
for i in range(10):
    current_number = int(input(f"Enter number {i + 1}: "))
    
    #checks the current_number against the unique_numbers list to see if it has already been entered if not it will be added to the unique_numbers list
    if current_number not in unique_numbers:
        unique_numbers.append(current_number)

print("\nNumbers entered (without duplicates):")
#loop through the final list to display them in the order they were entered
for number in unique_numbers:
    print(number)