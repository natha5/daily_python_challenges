

def convert_add(number_list):
    current_sum = 0
    for i in range(len(number_list)):
        current_value = int(number_list[i])
        number_list[i] = current_value
        current_sum = current_sum + current_value

    print(number_list)
    print(current_sum)


def check_duplicates(string_list):
    result_list = []
    list_length = len(string_list)
    for i in string_list:
        count_of_value = string_list.count(i)
        if count_of_value >1:
            result_list.append(i)
            check_for_result_dupes = result_list.count(i)
            if check_for_result_dupes >1:
                result_list.remove(i)
    if result_list == []:
        print("no duplicates")
        return "no duplicates"
    else:
        print(result_list)
        return result_list



convert_add(['12','4','8'])
check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark'])
