

def convert_add(number_list):
    current_sum = 0
    for i in range(len(number_list)):
        current_value = int(number_list[i])
        number_list[i] = current_value
        current_sum = current_sum + current_value

    print(number_list)
    print(current_sum)


convert_add(['12','4','8'])
