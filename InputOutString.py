class InputOutString():
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string : ")

    def printString(self):
        return self.s.upper()

inputOutString = InputOutString()
inputOutString.getString()    
upper_case_str = inputOutString.printString() 
print(upper_case_str)   
