def average(*args):
    total = 0
    for i in args:
        total = total + i
        avg = total/len(args)
    print(int(avg))

average(8,6,5,3)
nums = [9,1,3,4]
average(*nums)

//td[text()='Task4']//following-sibling::td[position()=count(//thead//th[text()='Start Date']//preceding-sibling::th)]//input