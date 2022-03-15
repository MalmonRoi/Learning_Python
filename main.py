def username_generator(first_name, last_name):
    if len(first_name) < 4:
        username = first_name
    else:
        username = first_name[0:3]
    if len(last_name) < 4:
        username += last_name
    else:
        username += last_name[0:4]
    return username


def password_generator(username):
    password = ""
    for iterate in range(0, len(username)):
        password += username[iterate - 1]
    return password