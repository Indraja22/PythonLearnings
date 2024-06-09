def deco_func_name_args(func):
    def wrapper(*args, **kwargs):
        name_func = func.__name__
        args_value = ', '.join(args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        # args_value = ', '.join(str(arg) for arg in args)
        print(f"Function name {name_func}, Args Value {args_value}, Keyword Args Value : {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@deco_func_name_args
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Indraja",greeting="Hi")
