#batch4_no4
all_numbers = []

print("Enter numbers one by one. Type any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    try:
        current_number = float(user_input)
        all_numbers.append(current_number)
    except ValueError:
        print("Invalid input detected. Stopping the program.")
        break

if all_numbers:
    #sorting the list of numbers in reverse order to print from highest to lowest
    all_numbers.sort(reverse=True)
    print(f"\nNumbers from highest to lowest: {all_numbers}")
else:
    print("\nNo valid numbers were entered.")