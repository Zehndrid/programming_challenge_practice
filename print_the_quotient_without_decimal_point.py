#batch1_no5
#input1
first_num = int(input("Enter the first number: "))
#input2
second_num = int(input("Enter the second number: "))

#getting the quotient without decimal point
total_quotient = first_num // second_num 

if second_num == 0:
    print("Math error")
#if the numbers are entered in wrong sequence
else:
    print("The total quotient is: " , total_quotient)
