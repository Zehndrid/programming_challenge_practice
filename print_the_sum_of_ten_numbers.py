#batch1_no7
total_sum = 0.0
# Using a for loop to repeat the input process 10 times
for i in range(10):
    # i starts at 0, so we use i + 1 to display "Enter number 1", "Enter number 2".
    current_number = float(input(f"Enter the number {i + 1 }: ")) 
    total_sum += current_number

print(f"The total sum of 10 numbers is {total_sum}")
    
