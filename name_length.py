def name_length(first_name, last_name):
    name = first_name + last_name
    if len(name) == 12:
        print(f"{first_name} {last_name} is exactly the average length of American names")
    elif len(name) > 12:
        print("Your name is longer than the average American names")
    else:
        print("Your name is shorter than the average American names")

name_length("Colt","Smith")
name_length("Marquese","Brownee")
name_length("Walton","Disney")
