#batach2_no1
#inputs
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if first_num < second_num:
    print("The smaller number is: ", first_num)
elif second_num < first_num:
    print("The smaller number is: ", second_num)
else:
    print("The numbers are equal")

