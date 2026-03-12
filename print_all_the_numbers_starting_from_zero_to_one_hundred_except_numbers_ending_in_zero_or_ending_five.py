#batch2_no9
#using for loop dividing by 10 and the result is not zero, the number does not end zero and does not end five
for current_number in range(101):
    if current_number % 10 !=0 and current_number % 10 !=5:
        print(current_number)