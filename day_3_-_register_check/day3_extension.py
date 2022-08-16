names = ["kerry", "dickson", "John", "Mary",
         "carol", "Rose", "adam"]

list_lowercase_names = []
tpl_lowercase_names = ()
for current_name in names:
    name_check = current_name.islower()
    if name_check:
        list_lowercase_names.append(current_name)
    list_lowercase_names.sort(reverse=True)
tpl_lowercase_names = tuple(list_lowercase_names)

print(tpl_lowercase_names)
