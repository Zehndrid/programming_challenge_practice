#batch2_no5
#inputs
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

#getting a math error if the first number is 0
if second_number == 0:
    print("Math error")
else:
    #calculating the remainder
    remainder_result = first_number % second_number
    print("The remainder when", first_number, "is divided by", second_number ,"is:" , remainder_result )