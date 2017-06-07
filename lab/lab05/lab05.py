## Mutable Lists ##

# Q1
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)):
        lst[i] = fn(lst[i])


# Q2
def over_nine_thousand(original_list):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> over_nine_thousand(original_list)
    >>> original_list
    [9001, 9002, 9003, 9004, 9005]
    """
    "*** YOUR CODE HERE ***"

    for i in range(len(original_list)):
        original_list[i] = original_list[i] + 9000

## Dictionaries ##

# Q4
def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for key in d:
        if(d[key] == x):
            d[key] = y




## Nonlocal ##

# Q5
def count_calls(f):
    """A function that returns a version of f that counts calls to f and can
    report that count to how_many_calls.


    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    "*** YOUR CODE HERE ***"
    n=0
    def counting():
        #nonlocal n
        return n
    def fixed(*args):
        nonlocal n
        n=n+1
        return f(*args)
    return fixed, counting

