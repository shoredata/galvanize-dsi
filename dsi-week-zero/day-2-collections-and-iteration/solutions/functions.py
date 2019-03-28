def reverse_index(lst,lx):
    """
    Write a function reverse_index that takes as arguments a list,
    and in integer index, and grabs the element from the list
    counting from the end of the list (where a usual index would be
    from the beginning).
    """
    #return lst[::-1][lx] #keeps array in memory, but is self-documenting
    #return lst[len(lst) -1 -lx] #also works
    return lst[-1-lx]

def in_or_error(lst,obj):
    """
    Write a function in_or_error that takes a list and any other
    python object as arguments. If the object lives inside of the
    list, return it, otherwise return a string containing a
    meaningful error message.
    """
    if obj in lst:
        return obj
    else:
        return f"Element {obj} not found"

def product_of_list(lst):
    result=1
    for x in lst:
        result *= x
        if result == 0: break
    return result

def double_elements(lst):
    '''
    idx=0
    for i in lst:
        lst[idx] *= 2
        idx+=1
    return lst
    '''
    return [num*2 for num in lst]

def double_append_list(lst):
    return lst+lst

def double_flop_list(lst):
    return lst+lst[::-1]

def search_for_divisibility(lst):
    return lst[0]

def fizz_buzz_sum(lst):
    '''Sums all numbers in a list that are either a multiple of 3 or 5.

    Parameters
    ----------
    numbers: list
      A list of integers.

    Returns
    -------
    sum: int
      The sum of all the numeric data in the list, excluding those summands
      not divisible by 3 or 5.
    '''
    sum=0
    for x in lst:
        if x%3==0 or x%5==0:
            sum+=x
    return sum
    pass

def search_for_divisibility(lst,num):
    """search list for first number div by num"""
    for x in lst:
        if x%num==0:
            return x;
    return 0;

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
    return list(zip(*matrix))


def make_zeros_matrix(x,y):
    result = []
    for i in range(x):
        newr = []
        for j in range(y):
            newr.append(0)
        result.append(newr)
    return result

def speckled_band_count(word):
    """
    Exercise: The Speckled Band
    Create a list containing all the words in the file
    `the_speckled_band.txt`.  Use this list to count how many times
    the word `Sherlock` appears in the story.
    Write a function `speckled_band_count` that counts how many
    times any word appears in the story.
    """
    count=0
    with open("../the_speckled_band.txt") as f:
        for line in f:
            words = line.lower().split()
            count+=words.count(word.lower())
    return count

def total_union(lst):
    """
    Write a function that computes the total union of a list of sets.
    """
    rtnset = set()
    for item in lst:
        #rtnset = rtnset.union(item)
        rtnset |= item     #same as above, |= is same as += for set
    return rtnset

def total_intersection(lst):
    """
    Write a function that computes the total intersection  of a list of sets.
    """
    rtnset = lst[0] #set()
    for item in lst:
        #rtnset = rtnset.union(item)
        rtnset &= item     #same as above, |= is same as += for set
    return rtnset


def negative_lookup(di,ix):
    """
    Write a function `negative_lookup` that takes a dictionary and an integer as arguments, and looks up the value stored under the *negative* of that integer.

    ```
    $ negative_lookup({1: 'one', -1: 'negative one'}, 1}
    "negative one"
    ```
    """
    return di[-ix]
    #for x in di.items(): #iterate over key=item
    #for x in di.values(): #iterate over values  .. refered to by di[x]

def split_vowel_consonant_punctuation(string):
    '''
    Split a string into three strings: one containing vowels, one containing
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
    sout = ['','','']
    for char in string:
        if char.lower() in 'aeiou':
            sout[0]+=char
        elif char.lower() in 'bcdfghjklmnpqrstvwxz':
            sout[1]+=char
        else:
            sout[2]+=char
    return sout


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
    #all methods on arrays work on memory in place, and they
    # return None!!!!
    numbers.sort()
    organized = []
    maxn = (numbers[-1]) // 10 + 1
    for i in range(maxn):
        row = []
        for item in numbers:
            if item >= i*10 and item < (i+1)*10:
                row.append(item)
        organized.append(row)
    return organized
