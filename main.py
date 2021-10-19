str_1 = input("Please enter a word: ")
str_sum_len = len(str_1)
sum_length = str_sum_len
last_letter = str_1[-1]
first_letter = ""
number_of_words = 1
while last_letter != first_letter:
    print(sum_length)
    last_letter = str_1[-1]
    str_1 = input("Please enter a word: ")
    str_sum_len = len(str_1)
    sum_length += str_sum_len
    first_letter = str_1[0]
    number_of_words += 1
print(number_of_words)
