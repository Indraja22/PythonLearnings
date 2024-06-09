def func_ex(age, *args, status="Single", **kwargs):
    print(f"parameter Age : {age}")
    print(f"args : {args}")
    print(f"default parameter : {status}")
    print(f"keyword arguments : {kwargs}")

func_ex(8,3,4,5,6,name="Sam")