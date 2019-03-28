from functions import f
from functions import m
from functions import sum_whole_numbers
from functions import (sign,first_larger,rev_sum,factorial,all_divisors,greatest_common_divisor)
from functions import (least_common_multiple,is_prime,nth_element_in_the_series,solver)

def test_solver():
    assert solver(75) == [1,2,3,4,5,6]
    assert solver(22) == [1,2,3,4,5,6]
    assert solver(38) == [1,2,3,4,5,6]
    assert solver(6) == [1,2,3,4,5,6]
    assert solver(57) == [1,2,3,4,5,6]
    assert solver(78) == [1,2,3,4,5,6]
    assert solver(80) == [1,2,3,4,5,6]
    assert solver(81) == [1,2,3,4,5,6]
    assert solver(88) == [1,2,3,4,5,6]
    assert solver(92) == [1,2,3,4,5,6]
    assert solver(100) == [1,2,3,4,5,6]
    assert solver(102) == [1,2,3,4,5,6]
    assert solver(104) == [1,2,3,4,5,6]
    assert solver(105) == [1,2,3,4,5,6]

def test_nth_element_in_the_series():
    assert nth_element_in_the_series(3) == 15
    assert nth_element_in_the_series(10) == 2047

def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(27) == False
    assert is_prime(13) == True

def test_least_common_multiple():
    assert least_common_multiple(4,11) == 44
    assert least_common_multiple(5,20) == 20

def test_greatest_common_divisor():
    assert greatest_common_divisor(6,9) == 3
    assert greatest_common_divisor(5,25) == 5

def test_all_divisors():
    assert all_divisors(4) == [1, 2, 4]
    assert all_divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]

def test_factorial():
    assert factorial(4) == 24
    assert factorial(6) == 720

def test_rev_sum():
    assert rev_sum(3) == 6
    assert rev_sum(5) == 15

def test_first_larger():
    assert first_larger(0,1) == False
    assert first_larger(1,0) == True

def test_f():
    assert f(6) == 7
    assert f(-1) == 0

def test_m():
    assert m(6,7) == 42
    assert m(42,0) == 0
    assert m(42,.5) == 21
    assert m(-21,-2) == 42
    assert m(21,-2) == -42

def test_sum_whole_numbers():
    assert sum_whole_numbers(3) == 6

def test_sign():
    assert sign(-1) == -1
    assert sign(0) == 0
    assert sign(1) == 1
