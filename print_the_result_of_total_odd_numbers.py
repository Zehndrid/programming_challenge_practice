#batch1_no8
total_odd = 0
#using for loop to get the odd numbers
for i in range(10):
    current_number = int(input(f"Enter the number {i + 1}: "))

#Check if the number is odd (if it has a remainder when divided by 2)
    if current_number % 2 != 0:
        total_odd += 1
        
print(f"The total odd numbers in 10 inputs are: {total_odd}")