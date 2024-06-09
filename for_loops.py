def for_loops_in_python():
    for i in range(0,11):
        print(i)

    print("================")
    nums = [3,4,5,7,1,9]
    for i in nums:
        print(i)

    for n in range(100,109):
        if(n % 2 == 0):
            print(f"{n} is an even number")
        else:
            print(f"{n} is an odd number")

    for k, v in zip(range(10),range(11,21)):
        print(f"{k} + {v}={k+v}")

    for k,v in zip(range(0,19), ["Kite","Kate",'Kane']):
        print(k,v)

    d = {"user_1":"active","user_2":"inactive","user_3":"active"}
    for k, v in d.items():
        print(f"{k} = {v}")

    l1 = [3,4,5,6,7,9,8]
    l1.sort()
    l2 = [3,4,5,7,9,8,6]    
    l2.sort()
    for i, j in zip(l1,l2):
       if (i == j):
            print(f"{i} is equal to {j}")
       else:
            print(f"{i} is not equal to {j}")

    students = ["Ronny","Sweety","Om","Sandy","Mandy"]
    roll_nos = [21, 29, 11, 71, 75]
    mapped = zip(students, roll_nos)
    print(dict(mapped))
    mapped = list(mapped)
    print(mapped)
    new_mapped = dict(mapped)
    print(new_mapped)
    for i, (name, age) in enumerate(zip(students, roll_nos)):
        if(i == 3):
            print(i, name, age)
    # std_roll_nums_dict = dict(mapped)
    # print(std_roll_nums_dict)
    for i, j in zip(students, roll_nos):
        print(f"{j} : {i}")  


for_loops_in_python()

