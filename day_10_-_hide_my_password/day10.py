def hide_password():
    password = input(print('Enter password : '))
    password_length = len(password)
    hidden_password = []
    for i in password_length:
        hidden_password.append('*')

    print('The password is ', password_length)
    return ''.join(hidden_password)


