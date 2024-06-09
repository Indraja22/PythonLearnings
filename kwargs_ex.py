def kwargs_ex(**kwargs):
    print(f"Values : {kwargs}")
    print(type(kwargs))

kwargs_ex(age=9, name="Tom")

def example_1(**kwargs):
    for k, v in kwargs.items():
        # print(f"{k} => {v}")
        print(k)
        print(type(kwargs.items()))
        print(type(k))
        print(type(v))

example_1(age=28,name="Indraja",company="Accenture")