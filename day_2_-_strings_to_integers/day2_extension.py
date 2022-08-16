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
    if not result_list:
        print("no duplicates")
        return "no duplicates"
    else:
        print(result_list)
        return result_list


check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark'])
