#batch4_no3
highest_number = None

print("Enter numbers one by one. Type any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    try:
        current_number = float(user_input)
        
        #the higher number will be printed until the user enters an invalid input
        if highest_number is None or current_number > highest_number:
            highest_number = current_number
            
    except ValueError:
        print("Invalid input detected. Stopping the program.")
        break
#decision statement to print the highest number or a message if no valid numbers were entered
if highest_number is not None:
    print(f"\nThe highest number entered is: {highest_number}")
else:
    print("\nNo valid numbers were entered.")