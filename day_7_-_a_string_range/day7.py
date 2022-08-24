
def string_range(input):
    current_output =[]
    for i in input:
        current_output[i] = str(i)

    output_string = ".".join(current_output)

    print(output_string)
    return output_string


string_range(6)
