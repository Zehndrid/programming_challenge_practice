#batch3_no4
lowest_number = None

print("Enter numbers one by one. Type any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    
    try:
        current_number = float(user_input)
        
        # If this is the very first number, OR if it's smaller than our current lowest
        if lowest_number is None or current_number < lowest_number:
            lowest_number = current_number
            
    except ValueError:
        print("Invalid input detected. Stopping the program.")
        break
#decision statement to print the lowest number or a message if no valid numbers were entered
if lowest_number is not None:
    print(f"\nThe lowest number entered is: {lowest_number}")
else:
    print("\nNo valid numbers were entered.")