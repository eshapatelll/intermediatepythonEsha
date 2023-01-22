def my_list(list):
    my_list = []
    for item in list:
        if item not in my_list:
            my_list.append(item)
    return my_list


test_list = [1, 2, 3, 2, 1, 4]
print(my_list(test_list))