
def count(input):
    my_dictionary = {}
    for char in input:
        if char in my_dictionary:
            my_dictionary[char] += 1
        else:
            my_dictionary[char] = 1
    return my_dictionary


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    my_group = {}
    for dictionary in input:
        if dictionary['key'] in my_group:
            my_group[dictionary['key']] += dictionary['value']
        else:
            my_group[dictionary['key']] = dictionary['value']
    return my_group


input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
]

print(group_by_key(input2))  # should print {'a': 6,'b': 1, 'c': 7}
