def two_list_dictionary(keys, values):

    output = {}

    for index, value in enumerate(keys):
        output[value] = values[index] if index < len(values) else None

    return output
    "Given keys and values, make dictionary of those."
    
print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
"{'x': 9, 'y': 8, 'z': 7}"
        
"If there are fewer values than keys, remaining keys should have value of None:"
    
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
"{'a': 1, 'b': 2, 'c': 3, 'd': None}"
    
"If there are fewer keys, ignore remaining values:"

print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
"{'a': 1, 'b': 2, 'c': 3}"