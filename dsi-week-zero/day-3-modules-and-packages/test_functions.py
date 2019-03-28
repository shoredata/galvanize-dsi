from functions import (function1, invert_dictionary, count_words, flatten_reduce_list)
from functions import (add_lists)

def test_function1():
    assert function1() == 0

def test_invert_dictionary():
    assert invert_dictionary({'a':1, 'b':2, 'c':1, 'd':3}) == {1: ['a', 'c'], 2:['b'], 3:['d']}

def test_count_words():
    assert count_words("../day-2-collections-and-iteration/the_speckled_band.txt") == 2885

def test_flatten_reduce_list():
    assert flatten_reduce_list([[1,2,3],[5,6],[7,8,9]]) == [1,2,3,5,6,7,8,9]

def test_add_lists():
    assert add_lists([1,2,3],[4,5,6]) == [5,7,9]
