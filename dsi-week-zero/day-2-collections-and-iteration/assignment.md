# Day 2 - Collection and Looping Assignment

This assignment revolves around using Python data structures well.

## Things to Think About

You are to fill in code for each of the function definitions below according to its documentation string. As you do, think about how data structures can help you write your code. Here are some questions you can ask yourself to figure out what data structure might help you:

1. Does the problem require order to be preserved?
2. Is some sort of membership being checked?
3. Is there a key-value relationship (implicit or explicit) that you can use a dictionary to describe?

Try to write tests for your functions!  In some of the documentations strings, we have provided some simple examples of expected behaviour, in others, this is up to you.  Try to think about edge cases as well!

## Problems

### Lists Only

```python
def fizz_buzz_sum(numbers):
    '''Sums all numbers in a list that are either a multiple of 3 or 5.

    Parameters
    ----------
    numbers: list
      A list of integers.

    Returns
    -------
    sum: int
      The sum of all the numeric data in the list, excluding those summands
      divisible by 3 or 5.
    '''
    pass
```

```python
def transpose(matrix):
    '''Transpose a matrix.  That is, reverse the roles of rows and columns

    $ transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

    Parameters
    ----------
    matrix: list of lists of numbers.

    Returns
    -------
    transposed: list of lists of numbers
      The transposed matrix.
    '''
    pass
```

```python
def split_vowel_consonant_punctuation(string):
    '''Split a string into three strings: one containing vowels, one containing
    consonants, and one containing punctuation.

    $ s = "My cat's name is Moshi!  She is old, but friendly."
    $ split_vowel_consonant_punctuation(s)
    ["aaeioieiouie", "MyctsnmsMshShsldbtfrndly", " '   !    ,  ."]

    Hint: Look up the `.join` method on strings!

    Parameters
    ----------
    string: str

    Returns
    -------
    vowel_consonant_punctuation: list of three strings.
      The first element in the list contains only vowels, the second only
      consonants, and the third only punctuation. 
    '''
    pass
```

```python
def make_triangle(n):
    '''Make a triangle containing the integers from 0 to (n+1)*n / 2

    $ make_triangle(2)
    [[1], [2, 3]]
    $ make_triangle(3)
    [[1], [2, 3], [4, 5, 6]]

    Parameters
    ----------
    n: positive integer

    Returns
    -------
    triangle: list of lists of integers
      A triangle continaing the consecutive integers
    '''
    pass
```

```python
def triangle_sum(triangle):
    '''Sum the diagonals of a triangle of numbers.

    $ triangle_sum([[1], [2, 3]])
    [2, 4]

    Because:
    [1]
    [2, 3] <- sum the diagonals
     2  4

    $ triangle_sum([[1], [2, 3], [4, 5, 6]])
    [4, 7, 10]

    Because:
    [1]
    [2, 3]
    [4, 5, 6] <- sum the diagonals
     4  7  10

    Parameters
    ----------
    triangle: list of lists of numbers

    Returns
    -------
    diagonal_sums: list of numbers
      The diagonal sums of the triangle.
    '''
    pass
```

```python
def pangram(string):
    '''Detects if a string contains every letter in the alphabet at least once. E.g.
       
        $ pangram("The quick brown fox jumps over the lazy dog")
	True
        $ pangram("Welcome to the jungle, we've got fun and games") 
        False

    Parameters
    ----------
    string: str

    Returns
    -------
    bool: Is the string a pangram?
    '''
    pass
```

### Free for All!

```python
def group_by_10s(numbers):
    '''Takes a list of numbers and groups the numbers by their tens place, giving
    every tens place it's own sublist. E.g.

    $ group_by_10s([1, 10, 15, 20])
    [[1], [10, 15], [20]]
    $ group_by_10s([8, 12, 3, 17, 19, 24, 35, 50])
    [[3, 8], [12, 17, 19], [24], [35], [], [50]]
                  
    Parameters
    ----------
    numbers: int
      A list of integers.
    
    Returns
    -------
    grouped: list of lists.
      List of lists of integers.  Each inner list collects all the values in
      the original list that share a tens digit.
    '''
    pass
```

```python
def word_sentence_paragraph_count(path, word):
    '''Takes in the path to a text file and a word returns a dictionary containing the following keys:

    {
        "word": The number times the word appears in the file.
	"sentence": The number of sentences the word appears in.
	"paragraphs": The number of paragraphs the word appears in.
    }

    Parameters
    ----------
    path: str
      A path to a text file.
    word: str
      A word to count in the file.

    Returns
    -------
    count_dict: dict
      The dictionary described above.
```

```python
def triple_double(string_1, string_2):
    '''Detects if a triple string of one character in one string has a
    matching double string of the same character in another. E.g.

    $ triple_double('aaa', 'ab')
    False
    $ triple_double("He's over 9000!", 'The roman numeral for 100 is C.')
    True

    Parameters
    ----------
    string_1 : str
    string_2 : str

    Returns
    -------
    bool
      Was there a triple-double in string_1 and string_2
    '''
    pass
```

```python
def same_sum(numbers):
    '''Takes a list of numbers and returns those whose digits sum to the same value
    as at least one other number in the list. E.g.

    same_sum([123, 23, 45, 90, 6, 7])
    $ [123, 45, 90, 6]

    Parameters
    ----------
    numbers : list of ints

    Returns
    -------
    list of ints
    '''
    pass
```

```python
def same_unique(list_1, list_2):
    '''Detects if two lists have the same counts of unique items regardless of
    what those items are. E.g.

    $ same_unique(['a', 'a', 'b'], [1, 1, 2])
    True
  
    # Both lists have two of one thing and one of another.

    $ same_unique(['a', 'a', 'b'], ['a', 'b']) => False
    ^ First list has two of one thing and one of another, second has one of two
    things.

    Parameters
    ----------
    list_1 : list
    list_2 : list

    Returns
    -------
    bool
    '''
    pass
```

### Extra Credit

1. Extend your pangram function to optionally require all 10 digits 0-9 to be present for a string to be a pangram. Your new function signature might look like:

 ```python
 def pangram(string, digits=False):
     ...
 ```

2. Extend the `triple_double` function to return all of the characters that meet the triple double requirement. Your new doc string might look like:

 ```python
 def triple_double(string_1, string_2):
     '''Finds all characters that appear three times in one string has a
     matching double string of the same letter in another. E.g.
 
     triple_double('aaa', 'aa') => ['a']
     triple_double("He's over 9000!!!", 'The roman numeral for 100 is C!!')
                                => ['0', '!']
 
     Parameters
     ----------
     string_1 : str
     string_2 : str
 
     Returns
     -------
     list of strings
     '''
 ```
