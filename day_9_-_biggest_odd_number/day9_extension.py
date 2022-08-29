def zeroes_last(input_list=[]):
    has_zeroes = False
    for i in input_list:
        if i == 0:
            input_list.pop(i)
            input_list.append(0)
            has_zeroes = True

    if not has_zeroes:
        input_list.sort()


zeroes_last([1, 4, 6, 0, 7, 0, 9])
