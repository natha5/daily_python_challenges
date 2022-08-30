def hide_password():
    password = input(print('Enter password : '))
    password_length = len(password)
    hidden_password = []
    for i in range(password_length):
        hidden_password.append('*')

    print('The password is ', password_length, ' character long')
    print(''.join(hidden_password))
    return ''.join(hidden_password)


hide_password()
