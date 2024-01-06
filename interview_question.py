input_str = "Python is a programming language. I know Python."

arr = input_str.split(" ")
newStr = ""
for i in arr:
    if(i == "Python"):
        i = "Java"
    newStr = newStr + " " + i

print(newStr)
