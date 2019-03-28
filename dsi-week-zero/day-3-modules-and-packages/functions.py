import collections
import functools
import itertools

def function1():
    return 0

def invert_dictionary(din):
    '''
    1.  "Invert" a dictionary using `defaultdict`.

    Since the keys of a dictionary are unique but the
     values need not be, it is not possible to simply
     switch the keys and values of a dictionary.

    For this exercise write a function that takes a
     dictionary as an argument and returns a
     dictionary whose keys are the values of the
     argument, and whose values are a `list` of all
     of the matching keys.

    For example, `invert_dictionary({'a':1, 'b':2, 'c':1, 'd':3})`
     should return `{1: ['a', 'c'], 2:['b'], 3:['d']}`.
    '''

    """
    dout = collections.defaultdict(list)
    for key,value in din:
        dout[value].append(key)
    return dout
    """
    inv = collections.defaultdict(list)
    for k, v in din.items():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv

def count_words(filepath):
    '''
    2. Count the words in a file with `collections.Counter`.

    Write a function that counts all of the words (separated
    by whitespace, removing digits and punctuation) and returns
    a `Counter` object with the results.

    To test this create a small file in the data directory.
    '''
    c = collections.Counter()
    with open(filepath) as infile:
        words = infile.read().split()
        c = collections.Counter(words)
    return len(c)

def flatten_reduce_list(lstin):
    '''
    3. Flatten a list with `reduce`.

    Write a function that flattens a list of lists with
    `functools.reduce` (if you're using Python 2, `reduce` is a
    built-in function).

    For example, `flatten([1,2,3],[5,6],[7,8,9])` should return
    `[1,2,3,4,5,6,7,8,9]`.

    You will need to write a function to pass to the reduce function
    or use `lambda`.
    '''

    return functools.reduce(lambda x,y: x+y ,lstin)

    #return [item for sublist in lstin for item in sublist]

    # #which means:
    # for sublist in l:
    #     for item in sublist:
    #         flat_list.append(item)
    # #is faster than the shortcuts posted so far. (l is the list to flatten.)
    # #Here is a the corresponding function:
    # flatten = lambda l: [item for sublist in l for item in sublist]

def add_lists(lst1,lst2):
    '''
    4. Add lists.

    Use `itertools.cycle` and `zip` to write a function
    `add_lists(list1, list2)` that takes lists and add them together
    element-wise.

    If the length of one is a multiple of the length of the
    other, a.

    If the length of one is the multiple of the length of the
    other, repeat the shorter before adding.

    If neither is a multiple of the other, raise a `ValueError`.
    '''
    #same size (doesn't use cycle:)

    if len(lst1) % len(lst2) != 0 and len(lst2) % len(lst1) != 0:
        raise ValueError("List lengths are *not* multiples of each other.")

    if len(lst1) < len(lst2):
        return [sum(item) for item in zip(itertools.cycle(lst1),lst2)]
    else:
        return [sum(item) for item in zip(lst1,itertools.cycle(lst2))]


# from sys import argv
# if __name__ == '__main__':
#     argv.pop(0) #remove first
#     print(sum([float(x) for x in argv]) / (len(argv))


import numpy as np

def rtn_std_array(np1da):
    '''
    Write a function that takes in a one-dimensional numpy array
    and standardizes it (i.e. subtracts off the mean and divides
    by the standard deviation). Return the standardized array.
    '''
    return (np1da - np.mean(np1da))/np.std(np1da)
ß
