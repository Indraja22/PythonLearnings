n = int(input("Enter the number of items in tuple : "))
ints = (input(f"Enter {n} space spearated integers : "))
sample_list = []
ints_list = ints.split(" ")
for i in ints_list:
    sample_list.append(int(i))

t = tuple(sample_list)
print(t)
print(hash(t))    

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))
