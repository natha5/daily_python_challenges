def zeroes_last(input_list=[]):
    has_zeroes = False
    for i in range(len(input_list)):
        if input_list[i] == 0:
            input_list.pop(i)
            input_list.append(0)
            has_zeroes = True

    if not has_zeroes:
        input_list.sort()

    print(input_list)
    return input_list


zeroes_last([2, 1 ,4, 7, 6])
