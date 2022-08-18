

def only_floats(a, b):
    type_a = type(a)
    type_b = type(b)

    if type_a == float and type_b == float:
        print(2)
        return 2
    elif type_a == float or type_b == float:
        print(1)
        return 1
    else:
        print(0)
        return 0


only_floats(12.1, 23)
