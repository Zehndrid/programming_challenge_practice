#batch3_no3
seen_numbers = []
#
print("Enter numbers one by one. Type any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    
    try:
        current_number = float(user_input)
        
        # Check if the number is already sitting inside our list
        if current_number in seen_numbers:
            print("Duplicate")
        else:
            print("Unique")
            # If it is unique, add it to the list so we remember it for next time!
            seen_numbers.append(current_number)
            
    except ValueError:
        print("Invalid input detected. Stopping the program.")
        break