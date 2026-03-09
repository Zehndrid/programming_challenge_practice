#input1
first_num = int(input("Enter the first number:"))
#input2
second_num = int(input("Enter the second number:"))
#decision part

if first_num > second_num:
    print("The first number is bigger")
elif second_num > first_num:
    print("The second number is bigger")
else:
    print("Both numbers are equal")