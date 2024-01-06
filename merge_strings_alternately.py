from itertools import zip_longest

def merge():
    word1 = "cf"
    word2 = "eee"
    return "".join(x+y for x, y in zip_longest(word1, word2, fillvalue=""))

print(merge())
