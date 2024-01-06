# s = input("Enter comma separated words : ")
# l = s.split(",")
# l.sort()
# s_sorted = ','.join(l)
# print(s_sorted)

# Question: Write a program that accepts a sequence of whitespace separated words as input 
# and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following 
# input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output 
# should be: again and hello makes perfect practice world

s = input("Enter whitespace separated words : ")
l = s.split(" ")
l.sort()
uniques_l = set(l)
# uniques_l = []
# for i in l:
#     if i not in uniques_l:
#         uniques_l.append(i)
sorted_unique_str = ' '.join(sorted(uniques_l))
print(sorted_unique_str)