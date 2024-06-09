try:   
    num = int(input("Enter a number : "))
except (ValueError,EOFError):
    print("I'll choose for you!")
    num = 9

print(f"You entered {num}")