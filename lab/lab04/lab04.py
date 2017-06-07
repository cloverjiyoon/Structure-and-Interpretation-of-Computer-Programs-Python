# Q2
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(i_list)):
    	if(i_list[i]>this):
    		print(i_list[i])
    	else:
    		print("that")


# Q4
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [[seq[i], fn(seq[i])] for i in range(len(seq)) 
    if fn(seq[i])>= lower and fn(seq[i]) <= upper]

# Q5
def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    if linked_lst == empty:
    	return []

    return [first(linked_lst)] + link_to_list(rest(linked_lst))

    
# Q6
def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    "*** YOUR CODE HERE ***"
    def flag(s0, s1, flagg):
    	flagg = flagg * -1
    	if flagg == 1:
    		if s0 == empty:
    			return s1
    		return link(bfirst(s0), flag(rest(s0),s1,flagg))
    	else:
    		if(s1 == empty):
    			return s0
    		return link(first(s1), flag(s0,rest(s1),flagg))

    return flag(s0, s1, -1)



# Linked List definition
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))


def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def isempty(s):
    """Returns True iff s is the empty list."""
    return s is empty

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)