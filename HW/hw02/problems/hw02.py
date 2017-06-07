HW_SOURCE_FILE = 'hw02.py'

#############
# Questions #
#############

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

from operator import add, mul

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"

    if(n==0):
        return base
    else:
        return combiner(accumulate(combiner,base,n-1,term),term(n))


def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)
def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)

def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate PRED.  COMBINER is a two-argument function.
    If v1, v2, ..., vk are the values in TERM(1), TERM(2), ..., TERM(N)
    that satisfy PRED, then the result is
         BASE COMBINER v1 COMBINER v2 ... COMBINER vk
    (treating COMBINER as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
    3600
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion'])
    True
    """
    def combine_if(x, y):
        if pred(y):
            return combiner(x, y)
        else:
            return x

    return accumulate(combine_if, base, n, term)

def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    """
    "*** YOUR CODE HERE ***"
    if n==0 :
        return lambda x: x
    else :
        return lambda x: f(repeated(f,n-1)(x))


def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h



def simple_prisoner_tournament(N, strategy1, strategy2):
    """Run N rounds of the Prisoner's Dilemma where STRATEGY1 and STRATEGY2
    are simple strategies used respectively by the two players.  Return
    a tuple (total1, total2) giving the cumulative sentences for the
    players using STRATEGY1 and STRATEGY2, respectively.
    >>> simple_prisoner_tournament(4, nice, nice)
    (4, 4)
    >>> simple_prisoner_tournament(5, rat, rat)
    (10, 10)
    >>> simple_prisoner_tournament(6, nice, rat)
    (18, 0)
    >>> simple_prisoner_tournament(2, rat, nice)
    (0, 6)
    >>> simple_prisoner_tournament(7, rat, tit_for_tat)
    (12, 15)
    >>> simple_prisoner_tournament(7, tit_for_tat, tit_for_tat)
    (7, 7)
    """

    "*** YOUR CODE HERE ***"

"*** YOUR CODE HERE ***"
nice = None        # Replace

"*** YOUR CODE HERE ***"
rat = None         # Replace

"*** YOUR CODE HERE ***"
tit_for_tat = None # Replace



def fancy_prisoner_tournament(N, strategy1, strategy2):
    """Run N rounds of the Prisoner's Dilemma where STRATEGY1 and STRATEGY2
    are fancy strategies used respectively by the two players.  Return
    a tuple (total1, total2) giving the cumulative sentences for the
    players using STRATEGY1 and STRATEGY2, respectively.
    >>> fancy_prisoner_tournament(4, nice2, nice2)
    (4, 4)
    >>> fancy_prisoner_tournament(5, rat2, rat2)
    (10, 10)
    >>> fancy_prisoner_tournament(6, nice2, rat2)
    (18, 0)
    >>> fancy_prisoner_tournament(2, rat2, nice2)
    (0, 6)
    >>> fancy_prisoner_tournament(7, rat2, tit_for_tat2)
    (12, 15)
    >>> fancy_prisoner_tournament(7, tit_for_tat2, tit_for_tat2)
    (7, 7)
    """
    "*** YOUR CODE HERE ***"

"*** YOUR CODE HERE ***"
nice2 = None        # Replace

"*** YOUR CODE HERE ***"
rat2 = None         # Replace

"*** YOUR CODE HERE ***"
tit_for_tat2 = None # Replace



def make_periodic_strategy(K):
    """Returns a fancy strategy that defects every K times it is called,
    and otherwise cooperates.
    >>> s = make_periodic_strategy(4)
    >>> fancy_prisoner_tournament(8, nice2, s)
    (12, 6)
    >>> fancy_prisoner_tournament(9, nice2, s)
    (13, 7)
    >>> fancy_prisoner_tournament(11, nice2, s)
    (15, 9)
    >>> fancy_prisoner_tournament(11, nice2, s)  # No side-effects
    (15, 9)
    >>> fancy_prisoner_tournament(12, s, make_periodic_strategy(3))
    (17, 14)
    """
    def periodic(i):
        """Returns a fancy strategy that defects every K times it is called,
        treating the first call as if it were the Ith call.  Thus, if K is
        3, then periodic(2) is a fancy strategy that first cooperates,
        then defects, then cooperates twice, then defects, cooperates twice,
        defects, etc."""
        "*** YOUR CODE HERE ***"
    return periodic(1)
