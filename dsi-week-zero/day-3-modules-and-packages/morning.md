# Modules and packages, Morning assignment

Most of the assignments for the morning should be done in a single file (call it `morning.py`). For each problem follow a test-driven approach. First, write an empty function signature, e.g.
```python
def add(a, b):
    '''Return the sum of a and b'''
    pass
```
If possible, write one or more assert statements:
```python
assert add(2, 3) == 5
```
For some of the functions it may not easy or possible, those that generate random variables or depend on your computer. If you can write assert statements, having several might help you consider less obvious cases.

Once you've done that run the program from the command line (`python morning.py`). You should get an AssertionError, but if you get a SyntaxError go back and fix it.

Finally, go back and write the function. Once you think it might be correct, run it from the command line to check. If it doesn't work, fix it before moving on.


## [collections](https://docs.python.org/3/library/collections.html)

1.  "Invert" a dictionary using `defaultdict`. Since the keys of a dictionary are unique but the values need not be, it is not possible to simply switch the keys and values of a dictionary. For this exercise write a function that takes a dictionary as an argument and returns a dictionary whose keys are the values of the argument, and whose values are a `list` of all of the matching keys. For example, `invert_dictionary({'a':1, 'b':2, 'c':1, 'd':3})` should return `{1: ['a', 'c'], 2:['b'], 3:['d']}`.

2. Count the words in a file with `collections.Counter`. Write a function that counts all of the words (separated by whitespace, removing digits and punctuation) and returns a `Counter` object with the results. To test this create a small file in the data directory.

## [functools](https://docs.python.org/3/library/functools.html)

3. Flatten a list with `reduce`. Write a function that flattens a list of lists with `functools.reduce` (if you're using Python 2, `reduce` is a built-in function). For example, `flatten([1,2,3],[5,6],[7,8,9])` should return `[1,2,3,4,5,6,7,8,9]`. You will need to write a function to pass to the reduce function or use `lambda`.

## [itertools](https://docs.python.org/3/library/itertools.html)

4. Add lists. Use `itertools.cycle` and `zip` to write a function `add_lists(list1, list2)` that takes lists and add them together element-wise. If the length of one is a multiple of the length of the other, repeat the shorter before adding. If neither is a multiple of the other, raise a `ValueError`.

Examples:
```
>>> add_lists([1, 2, 3], [4, 5, 6])
[5, 7, 9]
>>> add_lists([0, 10, 20], [1, 2, 3, 4, 5, 6])
[1, 12, 23, 4, 15, 26]
```

5. Hypothesis testing. Suppose you have an urn of balls. You have been told is filled with 12 red balls and 12 green balls, but you suspect the urn-contractor has mostly filled it with red balls (they are cheaper), so you decide too do a hypothesis test to check. You will pull 10 balls from the urn (without putting them back in) and if you get so many red balls that there is less than a 5% chance you would have seen at least that many by chance (assuming the 12/12 split) you're going to complain.

Write a function using itertools.combinations called `urn_test(n_red)` that will return the number of ways of getting at least `n_red` balls out of 10, assuming there are 12 red and 12 green balls, as above.

Hint: `collections.Counter` will also help, and the `count` method on `list` might make make it easier.

Generalize the function so it takes four arguments: the expected number of red balls, the expected number of green balls, the number you pick, and the number that are actually red.

Note that this will get very slow for large numbers. There are [more efficient ways](https://en.wikipedia.org/wiki/Hypergeometric_distribution) of solving this than calculating every combination

## [random](https://docs.python.org/3/library/random.html)

6. Roll dice. Write a function using `random.randint` called `roll(n_dice, n_sides)`. It will return a random result, the total of rolling `n_dice` that each have `n_sides` (that is, each die will give a random number between 1 and `n_sides` inclusive).

Non-deterministic functions are hard to test, but write at each least one assert statement to verify your code.

7. Hypothesis testing with simulations. Do the urn problem above with the same input and results, but using `random.sample` to choose simulate a test of drawing balls from the urn. Run it for a large number of simulations (at least a thousand) and return the fraction match. The results should be similar to the above function for a large number of samples.

## [sys](https://docs.python.org/3/library/sys.html)

8. Adding command-line arguments. Write a python program called `mean.py` that will use `sys.argv` to read the command-line arguments. The input should be numbers; it should convert them to `float`s, take the arithmetic mean, and return the result.

Most of the code should be in a `if __name__ == '__main__':` block, including reading `argv` and `print`ing the result. Use a function to compute the mean.


## [os](https://docs.python.org/3/library/os.html)

9. Write a function using `os.getenv` that returns all the directories in the PATH variable as a `list`. It will not take any arguments.

10. Counting lines in csv files. Write a function that takes a directory name as an argument, finds all files in that directory ending in `.csv`, and returns the total number of lines in all those files.
