#batch4_no5
total_sum = 0.0
number_count = 0

print("Enter numbers one by one. Type any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    try:
        current_number = float(user_input)
        
        # Add the number to our running total, and increase our tally by 1
        total_sum += current_number
        number_count += 1
        
    except ValueError:
        print("Invalid input detected. Stopping the program.")
        break

if number_count > 0:
    # Calculate the average and format it to 2 decimal places
    average = total_sum / number_count
    print(f"\nThe average is: {average:.2f}")
else:
    print("\nNo numbers were entered to calculate an average.")