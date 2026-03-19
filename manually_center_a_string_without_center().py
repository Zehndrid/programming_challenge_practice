#batch6_no7
user_string = input("Enter a string: ")
target_length = int(input("Enter total character length: "))

padding_needed = target_length - len(user_string)

if padding_needed > 0:
    # Integer division (//) splits the padding in half evenly
    left_padding = padding_needed // 2
    # The right padding gets whatever is left over (in case of an odd number)
    right_padding = padding_needed - left_padding
    
    result = (" " * left_padding) + user_string + (" " * right_padding)
else:
    result = user_string

print(f"Output: '{result}'")