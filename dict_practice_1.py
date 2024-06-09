users_dict = {"creds1":["Alex","Ibo78#@I"],"creds2":["Albert","Ibo90#@I"]}

for i,v in users_dict.items():
    # creds_list = users_dict[i]
    username = v[0]
    password = v[1]
    print(username)
    print(password)