
def string_range(input_value):
    current_output = []
    for i in range(input_value):
        string_value = str(i)
        current_output.append(string_value)

    output_string = ".".join(current_output)

    print(output_string)
    return output_string


string_range(6)
