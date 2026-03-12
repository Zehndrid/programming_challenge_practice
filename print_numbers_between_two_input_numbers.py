#batch2_no10
#inputs
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#using min and max to get the smaller and bigger number
start_number = min(first_number, second_number)
end_number = max(first_number, second_number)

#printing the numbers between the two input numbers
print(f"The numbers between {first_number} and {second_number} are:")

#using for loop to get the numbers between the two input numbers and end=" " to print the numbers in the same line
for current_number in range(start_number + 1, end_number):
   print(current_number, end=" ")