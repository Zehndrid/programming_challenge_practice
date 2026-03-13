#batch5_no7
user_statement = input("Enter a statement: ")

#using len() and .split() to count the number of words in the input
word_list = user_statement.split()
number_of_words = len(word_list)

print(f"Output: The number of words in the input is {number_of_words}.")