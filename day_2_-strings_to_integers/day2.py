

def convert_add(input_list):
    current_sum = 0
    for i in range(len(input_list)):
        current_value = int(input_list[i])
        input_list[i] = current_value
        current_sum = current_sum + current_value

    print(input_list)
    print(current_sum)


convert_add(['12','4','8'])