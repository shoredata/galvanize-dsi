# Day 4 - Objects and Classes Assignment

In this assignment we will write some classes to practice creating flexible data types.

## Things to Think About

Often the most crucial design decision you need to make when creating a class is when writing the `__init__` method.  You should always write the `__init__` method first.  Here are some things to think about:

  - What data does objects of this class need to store internally (i.e. what should the attributes of this class be).
  - What basic data structures (i.e. lists, tuples, sets, and/or dictionaries) are best for storing this internal data.

After implementing `__init__`, you have a class with basic functionality, and you should test out that everything works correctly by creating some objects and playing around with the attributes.  After that, you can start adding behaviour to the objects by adding methods.

## Problems: Without Magic Methods

### Password Validator
Write a password validator, which checks whether proposed passwords pass certain rules:

  - The password contains at least one capital letter.
<<<<<<< HEAD
  - The password contains at least one number.
=======
  - The password contains at least one numeric character.
>>>>>>> 71abb91b59dfc9ae856a966c692158e6aa858b81
  - The password contains at least one of a provided list of symbols.

```python
$ validator = PasswordValidator(symbols=['!', '?', '#'])
$ validator.validate('moshi')
False
$ validator.validate('moshi?')
True
$ validator = PasswordValidator(contains_capital=True, symbols=['!', '?', '#'])
$ validator.validate('moshi?')
False
$ validator.validate('Moshi?')
True
$ validator = PasswordValidator(contains_capital=True,
                                contains_number=True,
				symbols=['!', '?', '#'])
$ validator.validate('Moshi?')
False
$ validator.validate('M0shi?')
True
```

### VectorSegmenter

Write a class for segmenting and summarizing vectors (vectors are just python lists containing numeric data).

Segmenting should take a list of boolean values, and return a shorter list containing only the data that lines up with `True` values.

```python
$ v = VectorSegmenter([1, 2, 3, 4, 5, 6])
$ v.segment([True, True, False, False, True True])
[1, 2, 5, 6]
$ v.segment([True, False, True, False, True, False])
[1, 3, 5]
$ v.segment([False, False, False, False, False, False])
[]
```

For the summarization, you should have two methods `sum` and `average` that work as follows.

```python
$ v = VectorSegmenter([1, 2, 3, 4, 5, 6])
$ v.sum([True, True, False, False, True True])
14
$ v.average([True, True, False, False, True True])
3.5
$ v.sum([True, False, True, False, True, False])
9
$ v.average([True, True, False, False, True True])
3
```

### Room Generator (Hard)
Write a class that helps when generating rooms in video games.  Each room will be made up of walls inside a grid, with the walls outlining rectangles that you will add to the rooms.  When two of the rectangles added to the room overlap, the walls are deleted that occupy the interior of either of the rectangles.

Here's a demo of how it should work:

```python
$ from dungeon_room import DungeonRoom

$ room = DungeonRoom(10, 10)

$ room.add_rectangle(1, 2, 5, 6)

$ room.print_room()
. . . . . . . . . .
. . # # # # . . . .
. . # . . # . . . .
. . # . . # . . . .
. . # # # # . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .

$ room.add_rectangle(4, 4, 8, 9)

$ room.print_room()
. . . . . . . . . .
. . # # # # . . . .
. . # . . # . . . .
. . # . . # . . . .
. . # # . . # # # .
. . . . # . . . # .
. . . . # . . . # .
. . . . # # # # # .
. . . . . . . . . .
. . . . . . . . . .

$ room.add_rectangle(6, 2, 9, 7)

$ room.print_room()
. . . . . . . . . .
. . # # # # . . . .
. . # . . # . . . .
. . # . . # . . . .
. . # # . . # # # .
. . . . # . . . # .
. . # # . . . . # .
. . # . . . . # # .
. . # # # # # . . .
. . . . . . . . . .
```


## Problems: With Magic Methods

### Quadratic Polynomial
Write a class that represents a quadratic polynomial, that is, an algebraic expression like `a x^2 + b x + c`.  You should implement the following methods:

  - `evaluate`, which will plug in a number for `x` and evaluate the results.  It should return a single number.
  - Methods for adding and subtracting quadratic polynomials.
  - A method for testing if two quadratic polynomials are equal.
  - A `__repr__` method for displaying a quadratic polynomial to the console.

As a bonus (this is more difficult than you will anticipate):

  - Write a `__str__` method that prints a polynomial out in the usual way: `2 x^2 - x + 3`.  Pay attention to the edge cases!  Watch out for plus and minus signs, watch out for having coefficients of `1`, where it is usual to now write them.

### Currency Converter

Write a currency converter class.  Here's an example of how it should work.

```python
$ from currencies import CurrencyConverter
$ v1 = CurrencyConverter(23.43, "EUR")
$ v2 = CurrencyConverter(19.97, "USD")
$ v1
23.43 USD
$ v1.convert("USD")
27.72 USD
$ print(v1 + v2)
40.62 EUR
```
