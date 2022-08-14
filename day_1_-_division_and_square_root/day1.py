import math

def divide_or_square(input_value):
    result_of_mod = input_value % 5
    if result_of_mod == 0:
        sqrt_input = math.sqrt(input_value)

        return sqrt_input
    else:
        return result_of_mod





divide_or_square(10)