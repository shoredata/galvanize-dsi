def reverse_index(lst, idx):
    true_idx = len(lst) - idx - 1
    return lst[true_idx]

def in_or_error(lst, element):
    if element in lst:
        return element
    else:
        #return str(element) + " is not in list!"
        return "Hey {name}! {element} is not in list!".format(
            name="Matt", element=element)

def product_list(lst):
    acc = 1
    for number in lst:
        if number == 0:
            return 0
        acc = acc * number
    return acc


def double_list(lst):
    new_list = lst[:] 
    for item in lst:
        new_list.append(item)
    return new_list


def make_zero_matrix(n):
    zero_matrix = []
    for row_idx in range(n):
        row = [0 for i in range(3)]
        for col_idx in range(n):
            row.append(0)
        zero_matrix.append(row)
    return zero_matrix

def make_identity_matrix(n):
    identity_matrix = make_zero_matrix(n)
    for idx in range(len(identity_matrix)):
        identity_matrix[idx][idx] = 1
    return identity_matrix


def lookup_by_key(list_of_tuples, key):
    for tup in list_of_tuples:
        if tup[0] == key:
            return tup[1]
    return "Hey man, {} is not in your list of keys and values!".format(key)

def reverse_dictionary(D):
    new_dict = {}
    for key, value in D.items():
        new_dict[value] = key
    return new_dict

def dictionary_of_sums(list_of_numbers):
    D = {}
    for left_hand in range(len(list_of_numbers)):
        for right_hand in range(left_hand, len(list_of_numbers)):
            key = (list_of_numbers[left_hand], list_of_numbers[right_hand])
            value = key[0] + key[1]
            D[key] = value
    return D

def merge_dictionaries(dict1, dict2):
    new_dictionary = {}
    for key, value in dict2.items():
        new_dictionary[key] = value
    for key, value in dict1.items():
        new_dictionary[key] = value
    return new_dictionary
        








