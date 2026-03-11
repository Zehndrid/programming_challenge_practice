# batch2_no6
# Asking for the number separately for starting balancec
final_result = float(input("Enter number 1: "))

# Use a for loop to ask for the remaining 9 numbers
for i in range(1, 10):
    current_number = float(input(f"Enter number {i + 1}: "))
    
    # Subtract the new number from the running total
    final_result -= current_number

print(f"The result of the first number minus all the remaining numbers is: ", final_result)