# Problems with only lists

def fizz_buzz_sum(numbers):
    acc = 0
    for number in numbers:
        if number % 3 != 0 or number % 5 != 0:
            acc = acc + number
    return acc

def transpose(matrix):
    n_row = len(matrix)
    n_col = len(matrix[0])
    # Build empty matrix to build up
    transposed = []
    for i in range(n_col):
        transposed.append([])
    # Loop through the matrix in col, row order and append
    for col_idx in range(n_col):
        for row_idx in range(n_row):
            transposed[col_idx].append(matrix[row_idx][col_idx])
    return transposed

def split_vowel_consonant_punctuation(string):
    # We could use a set of letters here, it would be more efficient.
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # Build list of lists [[vowlels], [consonants], [puncuation]]
    vcp_lists = [[], [], []]
    for char in string:
        lower_char = char.lower()
        if lower_char in vowels:
            vcp_lists[0].append(char)
        elif lower_char in consonants:
            vcp_lists[1].append(char)
        else:
            vcp_lists[2].append(char)
    # Join vowel, consonant, puncuation lists into strings
    vcp_strings = []
    for lst in vcp_lists:
        vcp_strings.append(''.join(lst))
    return vcp_strings

def make_triangle(n):
    triangle = []
    current_number = 1
    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            inner_list.append(current_number)
            current_number = current_number + 1
        triangle.append(inner_list)
    return triangle

def triangle_sum(triangle):
    diagonal_sums = []
    for diagonal_number in range(len(triangle)):
        acc = 0
        for diagonal_position in range(len(triangle) - diagonal_number):
           acc = acc + triangle[diagonal_number + diagonal_position][diagonal_position]
        diagonal_sums.append(acc)
    return list(reversed(diagonal_sums))

def pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in string and letter.upper() not in string:
            return False
    return True

def pangram_with_set(string):
    # Clever solution with sets
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(string.lower()))


# Free for All!

def triple_double(str1, str2):
    triple_chars = _get_triple_chars(str1)
    double_chars = _get_double_chars(str2)
    triple_doubles = triple_chars & double_chars
    return triple_doubles != set()

def _get_triple_chars(str1):
    triple_chars = set()
    for idx in range(len(str1) - 2):
        three_chars = str1[idx:(idx+4)]
        if three_chars[0] == three_chars[1] and three_chars[1] == three_chars[2]:
            triple_chars.add(three_chars[0])
    return triple_chars

def _get_double_chars(str2):
    double_chars = set()
    for idx in range(len(str2) - 1):
        two_chars = str2[idx:(idx+3)]
        if two_chars[0] == two_chars[1]:
            double_chars.add(two_chars[0])
    return double_chars


def same_sum(numbers):
    # Dictionary whose keys are digit sums, and values are a list of numbers
    # with those digit sums.
    sum_dictionary = {}
    for number in numbers:
        # Sum the digits of the numbers by converting the number into a list of
        # its digits (as strings), then summing up the digits.
        digits_as_strings = list(str(number))
        digit_sum = 0
        for digit_string in digits_as_strings:
            digit_sum = digit_sum + int(digit_string)
        # Add this digit sum to the dictionary
        if digit_sum in sum_dictionary:
            sum_dictionary[digit_sum].append(number)
        else:
            sum_dictionary[digit_sum] = [number]
    # Now join together all the lists that have more than one number in
    # them.
    return_list = []
    for digit_sum, numbers in sum_dictionary.items():
        if len(numbers) >= 2:
            return_list.extend(numbers)
    return return_list
