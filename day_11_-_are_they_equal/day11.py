
def equal_strings(string_one, string_two):
    len_one = len(string_one)
    len_two = len(string_two)

    are_equal = False

    if len_one == len_two:
        are_equal = True
    else:
        print(are_equal)
        return are_equal

    for i in string_one:
        string_two.find(i)
        if i == -1:
            are_equal = False
            print(are_equal)
            return are_equal
        else:
            are_equal = True

    print(are_equal)


equal_strings('love', 'evol')

