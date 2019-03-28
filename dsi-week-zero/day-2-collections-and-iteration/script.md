# Python Workshop: Collections and Iteration

Today we will be learning about two foundational topics in programming:

  - **Collections** are a class of data types that gather together conceptually related data into a whole.  For example, we could have a list of numbers, or a set of strings.  We will discuss three main types of collections today: *lists*, *tuples*, *sets*, and *dictionaries*.

  - **Iteration** is the process of visiting each member of a collection, and taking an action on it.  For example, we could visit all the strings in a list and join the various words into a sentence, or we could visit all the numbers in a set and calculate the sum of them all.

We will be introducing these two important concepts together, as they tend to depend upon and enhance one another.  Here is the overall plan:

#### Lists

  - Introduce Lists.
  - What can go in lists?
  - Indexing and slicing into a list.
  - The `in` operator.
  - `for` loops, and visiting all the elements in a list.
  - Building a list incrementally using `append`.
  - Searching and `break`
  - Mutability of lists, index assignment.
  - Looping over files.

#### Tuples

  - Mutability of lists.
  - Wat's with the mutability of lists.
  - Tuples: immutable lists.

#### Sets

  - Introduce sets.
  - Visiting all the elements in a set.
  - Operations on sets.
  - Building a set incrementally with `add`.
  - The `in` operator.
  - Efficiency of sets vs. lists: why have both?
  - Solving problems with sets.

#### Dictionaries

  - Lists of tuples as key-value pairs.
  - Introduce dictionaries.
  - Indexing into a dictionary and `.get`.
  - Building a dictionary incrementally.
  - Efficiency of dictionaries vs. lists of tuples.
  - Restrictions on dictionary keys.
  - Solving problems with dictionaries.
  

## Lists

### Introduce Lists

  - List literal notation `[...]`.
  - What can go in lists?
  - Length of a list.

### Indexing and Slicing a List

  - Indexing into a list.

#### Exercise: Reverse Indexing
Write a function `reverse_index` that takes as arguments a list, and in integer index, and grabs the element from the list counting from the *end* of the list (where a usual index would be from the beginning).

```python
$ reverse_index([1, 2, 3, 4], 0)
4
$ reverse_index([1, 2, 3, 4], 3)
1
$ reverse_index([1, 2, 3, 4], 1)
3
```

  - Slicing a list

#### Exercise: Reverse Slicing
Write a function `reverse_slice` that takes as arguments a list, and two non-negative integers `left` and `right`, and slices the list in reverse.

```python
$ reverse_slice([1, 2, 3, 4], 0, 1)
[3, 4]
$ reverse_slice([1, 2, 3, 4], 0, 2)
[2, 3, 4]
$ reverse_slice([1, 2, 3, 4], 1, 2)
[2, 3]
```

###  The `in` operator.

  - Checking containment with the `in` operator.

#### Exercise: In or Error
Write a function `in_or_error` that takes a list and any other python object as arguments.  If the object lives inside of the list, return it, otherwise return a string containing a meaningful error message.

```python
$ in_or_error([2, 4, 6], 4)
4
$ in_or_error([2, 4, 6], 5)
"Element 4 is not in list!"
$ in_or_error(["hello", "kitty"], "kitty")
"kitty"
$ in_or_error(["hello", "kitty"], "puppy")
"Element puppy is not in list!"
```

Note: We will later develop much better ways to signal errors.

### `for` loops, and visiting all the elements in a list.

  - For loops, and visiting all the elements in a list.
  - The accumlator pattern: summing a list.

#### Exercise: Product
Write a function `product` that computes the product of all products in a numeric list.

  - `break` and quitting early.

#### Exercise: Product Revisited
Write an improved version of `product` that bails out early if it detects that the resulting product must be zero.

###  Building a list incrementally using `append`.

  - The `append` method.
  - The builder pattern.

#### Exercise: Doubling a List
Write a function `double_elements` which takes a numeric list, and returns a new list of the same length where all the elements are doubled.

```python
$ double_elements([0, 1, 2, 3])
[0, 2, 4, 6]
```

#### Exercise: Doubling a List (Revisited)
Write a function `double_list` which takes a list, and returns two copies of the list concatenated together.

```python
$ double_list([0, 1, 2, 3])
[0, 1, 2, 3, 0, 1, 2, 3]
```

#### Exercise: (Doubling a List (Revisited)) (Revisited)
Write a function `double_flop_list` which takes a list, and returns two copies of the list concatenated together, but with the rightmost copy *reversed*.

```python
$ double_list([0, 1, 2, 3])
[0, 1, 2, 3, 3, 2, 1, 0]
```

### Searching and `break`

  - Searching a list with the `break` statement.

#### Exercise: Searching for a Number
Write a function that returns the first number in a list that is divisible by a given number

```python
$ search_for_divisibility([2, 4, 6, 8, 10, 12, 12, 10, 8], by=3)
6
$ search_for_divisibility([2, 4, 6, 8, 10, 12, 12, 10, 8], by=5)
10
```

#### Exercise: Searching Words
Write a function that returns the first word in a list of words that is in all lower case.

```python
words = ["Moshi", "Caitlyn", "FORTRAN", "C", "cat", "dog", "HTTP", "Jack"]
$ seach_for_all_lower_case(words)
"cat"
```

###  Mutability of lists, index assignment.

  - Index assignment.
  - Mutability, WUT.

#### Exercise: Zero Matrix
Write a function that creates a matrix of zeros with a specified number of rows and columns.  A matrix is a list of lists, where each entry in one of the inner lists is a number.

```python
$ make_zeros_matrix(2, 2)
[[0, 0], [0, 0]]
$ make_matrix_zeros(2, 3)
[[0, 0, 0], [0, 0, 0]]
$ make_matrix_zeros(3, 2)
[[0, 0], [0, 0], [0, 0]]
```

#### Exercise: Identity Matrix
Write a function that creates an *identity* matrix of a given size.  An identity matrix is a square matrix (same number of rows and columns), that has ones on the diagonal.

```python
$ make_identity_matrix(2)
[[1, 0], [0, 1]]
$ make_identity_matrix(3)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

### Exercise: Row and Column Sums
Write a function `row_or_column_sum` which takes as arguments
  - A matrix.
  - A string which is either "row" or "sum".
The function should return a numeric list, which contains either the row or column sums of the matrix, as specified.

```python
$ M = [[0, 1], [0, 2], [0, 3]]
$ row_or_column_sum(M, "row")
[1, 2, 3]
$ row_or_column_sum(M, "column")
[0, 6]
```

### Looping over Files

  - The `with` statment and `open`.
  - Looping through an open file line by line.

#### Exercise: The Speckled Band
Create a list containing all the words in the file `the_speckled_band.txt`.  Use this list to count how many times the word `Sherlock` appears in the story. Write a function `speckled_band_count` that counts how many times any word appears in the story.


### Tuples

  - Mutability of lists.
  - Wat's with the mutability of lists.
  - Tuples: immutable lists.

#### Exercise: Sequence of Tuples
Write a function that takes as argument a positive integer `n`, and returns a list of tuples of the form (i, i+2), with i ranging from zero to `n`.

```python
$ list_of_tuples(4)
[(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)]
```


## Sets

### Introduce sets.

  - Set literal notation.
  - Unordered collections.


### Visiting all the elements in a set.
### Operations on sets.

  - The union of two sets.
  - The intersection of two sets.
  - The difference of two sets.

#### Exercise: The Total Union

Write a function that computes the total union of a list of sets.

```python
$ total_union([{1, 2}, {2, 3}, {3, 4}])
{1, 2, 3, 4}
$ total_union([{1, 2, 3, 4}, {1, 2, 3}, {1, 2}])
{1, 2, 3, 4}
```

#### Exercise: The Total Intersection

Write a function that computes the total intersection of a list of sets.

```python
$ total_intersection([{1, 2}, {2, 3}, {3, 4}])
{}
$ total_intersection([{1, 2, 3, 4}, {1, 2, 3}, {1, 2}])
{1, 2}
```

### Building a set incrementally with `add`.

  - The `.add` method and the builder pattern.
  - Yup, this means sets are mutable.

#### Exercise: List to Set
Write a function `list_to_set` that converts a list into a set

```python
$ list_to_set([1, 2, 3, 4])
{1, 2, 3, 4}
$ list_to_set([])
set([])
```

#### Exercise: The Set of Primes

Write a function that takes as argument a positive integer `n`, and returns the set of prime numbers less than or equal to `n`.

```python
$ primes(10)
{2, 3, 5, 7}
$ primes(100)
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
```

### The `in` operator.

  - Efficiency of the `in` operator for lists vs. sets.
  - Reading in a file.
  - Checking whether a word is in a book, list vs. set.

#### Exercise: The Speckled Band Revisited
Create both a set and a list containing all the words in `the_speckled_band.txt`.  Use the set and list to check whether various words are contained in the story.  Time the inclusion checks for the set vs. the list.


## Dictionaries

#### Exercise: List of Tuples

Consider the case of lists-of-tuples.  Here's an example where the first element of each tuple is a post-punk band, and the second element of each tuple is an important album they recorded

```python
post_punk_albums = [
    ("Wire", "Pink Flag"),
    ("Gang of Four", "Entertainment!"),
    ("Joy Division", "Unknown Pleasures"),
    ("Pere Ubu", "Dub Housing"),
    ("Public Image Ltd", "First Issue")
]
```

We can think of a data structure like this as a *mapping* from bands to albums.  In abstract, we will refer to the first element of such a tuple as a **key** and the second as a **value**.

Write a function that consumes a list of two-tuples and the value of a key, and returns the value stored in the tuple with that key.  For example

```
$ lookup_by_key(post_punk_albums, "Pere Ubu")
"Dub Housing"
```


### Introduce Dictionaries

  - Dictionary literal notation.

### Indexing into a Dictionary

  - Looking up by key.

#### Exercise: A Negative Dictionary
Write a function `negative_lookup` that takes a dictionary and an integer as arguments, and looks up the value stored under the *negative* of that integer.

```
$ negative_lookup({1: 'one', -1: 'negative one'}, 1}
"negative one"
```

### Efficiency of dictionaries vs. lists of tuples.

### The `.get` Method and `in`

#### Exercise: Positive or Negative Lookup
Write a function `positive_or_negative_lookup` that takes a dictionary and an integer as arguments.  If the integer is a key in the dictionary, return the value stored under that key.  Otherwise, if the negative of the integer is a key in the dictionary, return the value stored under the negative of the key.  If both of these fail, return `False`.

```
$ positive_or_negative_lookup({1: 'one', -2: 'negative two'}, 1)
"one"
$ positive_or_negative_lookup({1: 'one', -2: 'negative two'}, 2)
"negative two"
$ positive_or_negative_lookup({1: 'one', -2: 'negative two'}, 3)
False
```

### Building a Dictionary Incrementally

  - Creating empty dictionaries
  - Building a dictionary incrementally

#### Exercise: Alphabet Dictionary
Create a dictionary whose keys are letters in the alphabet, and whose values are their *poisition* within the alphabet.

#### Exercise: Dictionary Reversal
Write a function `reverse_dictionary` that swaps the roles of keys and values in a dictionary.

```python
$ reverse_dictionary({'a': 1, 'b': 2, 'c': 3})
{1: 'a', 2: 'b', 3: 'c'}
```

### Restrictions on Dictionary Keys

#### Exercise: Number Pairs
Write a function that consumes a list of numbers, then returns a dictionary whose keys are *pairs* of these numbers, and whose values are the sum of the two numbers.  For example, under the pair 2, 3, we would store the sum number 5.

```python
$ dict_of_sums([1, 2, 3])
{(0, 0): 2, (0, 1): 3, (0, 2): 4, (1, 1): 4, (1, 2): 5, (2, 2): 6}
```

  - Tuples as keys.
  - Lists as keys?
  - Re-using keys.

#### Exercise: Dictionary Reversal Revisited
As we have seen, when we add a key to a dictionary multiple times, the value gets overwritten.  This has consequences for reversing a dictionary

```python
$ reverse_dict({'a': 1, 'b': 2, 'c': 2}) 
{1: 'a', 2: 'c'}
```

Fix this issue in your `reverse_dictionary` function by instead creating a dictionary of lists.

```python
$ reverse_dict({'a': 1, 'b': 2, 'c': 2})
{1: ['a'], 2: ['b', 'c']}
```

### Looping over dictionaries.

  - Looping over the keys in a dictionaries
  - Other looping options: python 2 vs. python 3

#### Exercise: Merging Dictionaries
Write a function `merge_dictionaries` which takes two dictionaries are arguments, and returns a *merged* dictionary.  That is, one containing any key, value pair that appears in *either* dictionary.
