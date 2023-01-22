def combined_dict(my_dict_1, my_dict_2):
    
    result = {}
    
    for key in my_dict_1:
        
        if key in my_dict_2:
            result[key] = my_dict_1[key] + my_dict_2[key]
    return result


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = combined_dict(my_dict_1, my_dict_2)
print(combined_dict)