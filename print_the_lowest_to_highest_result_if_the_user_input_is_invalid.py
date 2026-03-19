#batch3_no5
all_numbers = []

print("Enter numbers one by one. Type any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    
    try:
        current_number = float(user_input)
        #safely gather all the valid numbers into our list
        all_numbers.append(current_number)
    except ValueError:
        print("Invalid input detected. Stopping the program.")
        break

if all_numbers:
    #the sort() function automatically arranges the list from lowest to highest
    all_numbers.sort()
    print(f"\nNumbers from lowest to highest: {all_numbers}")
else:
    print("\nNo valid numbers were entered.")