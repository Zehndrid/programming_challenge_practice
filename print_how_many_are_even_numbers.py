#batch2_no7
even_count = 0
#using for loop to get the odd numbers
for i in range(10):
    current_number = int(input(f"Enter the number {i + 1}: "))

#Check if the number is even and making sure it is equal to zero
    if current_number % 2 == 0:
        even_count += 1
        
print(f"The total even numbers in 10 inputs are: {even_count} ")