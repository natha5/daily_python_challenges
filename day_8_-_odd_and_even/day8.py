

def odd_even(input_list):

    largest_even = 0
    smallest_odd = 9999999
    for i in input_list:

        if i % 2 == 0:
            if i > largest_even:
                largest_even = i
        elif i < smallest_odd:
            smallest_odd = i

    result = largest_even - smallest_odd

    print(largest_even , " - " , smallest_odd , " = " , result)

    return result


odd_even([1, 2, 4, 6])
