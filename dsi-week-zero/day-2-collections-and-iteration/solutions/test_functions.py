from functions import (reverse_index, in_or_error, product_of_list, double_elements)
from functions import (double_append_list, double_flop_list, fizz_buzz_sum)
from functions import (search_for_divisibility, transpose, make_zeros_matrix)
from functions import (speckled_band_count, total_union, negative_lookup, total_intersection,split_vowel_consonant_punctuation)
from functions import (group_by_10s)

def test_reverse_index():
    assert reverse_index([0,1,2,3,4,5,6,7,8,9],5) == 4

def test_in_or_error():
    assert in_or_error([2,4,6],4) == 4
    assert in_or_error([2,4,6],5) == "Element 5 not found"
    assert in_or_error(["hello", "kitty"], "kitty") == "kitty"
    assert in_or_error(["hello", "kitty"], "puppy") == "Element puppy not found"

def test_product_of_list():
    assert product_of_list([1,2,3]) == 6
    assert product_of_list([0,1,2]) == 0

def test_double_elements():
    assert double_elements([2,4,6]) == [4,8,12]

def test_double_append_list():
    assert double_append_list([2,4,6]) == [2,4,6,2,4,6]

def test_double_flop_list():
    assert double_flop_list([2,4,6]) == [2,4,6,6,4,2]

def test_fizz_buzz_sum():
    assert fizz_buzz_sum([0,1]) == 0
    assert fizz_buzz_sum([0,1,3]) == 3
    assert fizz_buzz_sum([0,1,3,9,15,16]) == 27

def test_search_for_divisibility():
    assert search_for_divisibility([1,2,3,10,15,24],3) == 3
    assert search_for_divisibility([1,2,3,10,15,24],13) == 0
    assert search_for_divisibility([1,2,3,10,15,24],8) == 24

def test_transpose():
    assert transpose([[1,2,3],[4,5,6]]) == [(1,4),(2,5),(3,6)]

def test_make_zeros_matrix():
    assert make_zeros_matrix(2,2) == [[0,0],[0,0]]

def test_speckled_band_count():
    assert speckled_band_count("the") == 586
    assert speckled_band_count("sherlock") == 9
    assert speckled_band_count("BIRD") == 1

def test_total_union():
    assert total_union([{1, 2}, {2, 3}, {3, 4}]) ==  {1, 2, 3, 4}

def test_total_intersection():
    assert total_intersection([{1, 2}, {2, 3}, {2, 4}]) ==  {2}

#def test_negative_lookup():
#    assert negative_lookup({'a':-1,'b':-2,'c':3},1) == '1'

def test_split_vowel_consonant_punctuation():
    assert split_vowel_consonant_punctuation("IUykjbiuh(ij098kjbu 8897(*&b gh(*Ykljb*Y*hkjb))") == ['IUiuiu', 'kjbhjkjbbghkljbhkjb', 'y(098 8897(*& (*Y*Y*))']

def test_group_by_10s():
    #assert group_by_10s([12,5,2,24,32,98,101,4,0,12,56,88,534]) == [1,12,23]
    assert group_by_10s([8, 12, 3, 17, 19, 24, 35, 50]) == [[3, 8], [12, 17, 19], [24], [35], [], [50]]
    assert group_by_10s([1, 10, 15, 20]) == [[1], [10, 15], [20]]
