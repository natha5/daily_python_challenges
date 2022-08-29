
def biggest_odd(str_input):
    char_list = list(str_input)

    largest_odd = 0

    for i in char_list:
        i_to_int = int(i)
        if i_to_int % 2 == 1:
            if i_to_int > largest_odd:
                largest_odd = i_to_int
    print(largest_odd)
    return largest_odd


biggest_odd('23569')
