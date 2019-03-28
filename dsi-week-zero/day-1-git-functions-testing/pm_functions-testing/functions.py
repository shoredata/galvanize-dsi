import math
from math import sqrt
from itertools import count, islice


def f(x):
    return x + 1

def m(a,b):
    return a * b

def sum_whole_numbers(x):
    """
    Write a function that returns the sum of the whole numbers between 1 and a specified number.
    """
    result = 0
    for i in range (x+1):
        result += i
    return result

def sign(x):
    """
    Write a function sign(x) that takes a specified number and returns whether it is positive, negative or zero. If the number is positive, return 1. If the number is negative, return -1. If the number is zero, return 0.
    """
    if x < 0:
       return -1
    elif x == 0:
       return 0
    else:
       return 1

def first_larger(x,y):
    """
    Write a function that takes two numbers, a and b, and returns True if the first number is larger or False if it's not.
    """
    if x > y:
        return True
    else:
        return False

def rev_sum(x):
    """
    Write a function that computes the sum from 0 to a specified number. This time though, start at the specified number and work down.
    """
    result = 0
    for i in range (x,0,-1):
        result += i
    return result


def factorial(x):
    """Write a function that computes the factorial of a specified number. """
    result = 1
    for i in range (1,x+1,1):
        result *= i
    return result

def all_divisors(x):
    """
    Write a function that computes and returns all of the divisors of a specified number.
    """
    divs = [1]
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            divs.extend([i,int(x/i)])
    divs.extend([x])
    slist = list(set(divs))
    slist.sort()
    return slist

def greatest_common_divisor(x,y):
    """
    As of Python 3.5, gcd is in the math module; the one in fractions is deprecated. Moreover, inspect.getsource no longer returns explanatory source code for either method.

    also:
        while b:
            a, b = b, a"%"b
        return a
    """
    return math.gcd(x,y)

def least_common_multiple(x,y):
    """
    Write a function that computes the least common multiple between two specified numbers.
    """
    return x * y // greatest_common_divisor(x, y)
    pass

def is_prime(x):
    """
    Write a function that determines whether or not a specified number is a prime number and returns True or False depending on what your function finds.
    """
    if x < 2: return False
    for number in islice(count(2), int(sqrt(x)-1)):
        if not x%number:
            return False
    return True

def nth_element_in_the_series(n):
    """
    Write a function that returns the nth element in the series s.
    The nth item will be 1-based, ie 6 = the 6th 1-based item in list.
    ---
    a(i=0) = 1, a(i) = 2*a(i-1) + 1, for i>0
    """
    a = 1
    for i in range(n):
        a = 2*a + 1
    return a

def solver(result):
    """
    Challenge: solve the equation:
        (a + (b - c) * d - e) * f = 75
        where a, b, c, d, e, and f are unique integers in the range [1, 6].

    Hints:
        Computers are so fast that your program can simply try all possible valid values of a, b, c, d, e, and f until it finds one permutation of 1-6 that solves the challenge! (Btw, there is only one permutation that will solve it.)
        Use 6 nested for-loops to enumerate all ways of setting each of a, b, c, d, e, and f to the values 1-6.
        Use if-statements to ensure all values of a, b, c, d, e, and f are valid. (I.e. to ensure that each value is unique)
        Use an if-statement to test if the current permutation solves the challenge.
    """
    pass
