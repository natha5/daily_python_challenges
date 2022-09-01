
def count_dots(input_string):
    string_as_list =  list(input_string)
    count_of_dots = 0
    for i in string_as_list:
        if i == '.':
            count_of_dots = +1

    print(count_of_dots)
    return(count_of_dots)
