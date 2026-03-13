#batch5_no2
#input number from 0-1000
user_number = (input("Enter a number from 0 to 1000: "))

#using zfill() to print six digits with three zeros in the left
formatted_number = user_number.zfill(6)
print(f"Output: {formatted_number}")