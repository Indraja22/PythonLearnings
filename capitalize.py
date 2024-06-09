def capitalize_str(input_str: str):
    input_str_list = input_str.split()
    new_str = []
    for i in input_str_list:
        i_cap = i.capitalize()
        new_str.append(i_cap)
    return " ".join(new_str).strip()

print(capitalize_str("indraja naik"))
print(capitalize_str("12abc"))
print(capitalize_str("hello   world  lol"))

def capitalize_str_1(input_str: str):
    pass
