import emoji


def Python_snakes(input_value):
    for i in range(input_value):
        for j in range(i):
            print(emoji.emojize(':snake:'), end = ' ')
        print(' ')


Python_snakes(7)