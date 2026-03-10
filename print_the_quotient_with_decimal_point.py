#batch1_no5
#input1
first_num = float(input("Enter the first number: "))
#input2
second_num = float(input("Enter the second number: "))

#getting the quotient with decimal point
total_quotient = first_num / second_num 

if second_num > first_num:
    print("Syntax error")
#if the numbers are entered in wrong sequence
else:
    print(f"The total quotient is: {total_quotient:.2f}")
