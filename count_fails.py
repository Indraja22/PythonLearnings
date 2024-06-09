def count_fails(*scores):
    count = 0
    for score in scores:
        if score <= 50:
            count = count + 1
    return count

nums  = [8,4,3,11,89,91,100,50,23]
print(count_fails(*nums))