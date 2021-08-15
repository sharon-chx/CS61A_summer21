def deep_map_mut(fn, lst):
    """Deeply maps a function over a Python list, replacing each item
    in the original list object.

    Does NOT create new lists by either using literal notation
    ([1, 2, 3]), +, or slicing.

    Does NOT return the mutated list object.

    >>> l = [1, 2, [3, [4], 5], 6]
    >>> deep_map_mut(lambda x: x * x, l)
    >>> l
    [1, 4, [9, [16], 25], 36]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)):
        if type(lst[i]) == list:
            deep_map_mut(fn, lst[i])
        else:
            lst[i] = fn(lst[i])



from operator import add, sub, mul

def foldl(s, f, start):
    """Return the result of applying the function F to the initial value START
    and the first element in S, and repeatedly applying F to this result and
    the next element in S until we reach the end of the list.

    >>> s = [3, 2, 1]
    >>> foldl(s, sub, 0)      # sub(sub(sub(0, 3), 2), 1)
    -6
    >>> foldl(s, add, 0)      # add(add(add(0, 3), 2), 1)
    6
    >>> foldl(s, mul, 1)      # mul(mul(mul(1, 3), 2), 1)
    6

    >>> foldl([], sub, 100)   # return start if s is empty
    100
    """
    "*** YOUR CODE HERE ***"
    if len(s) == 1:
         return f(start, s[0])
    return foldl(s[1:], f, f(start, s[0]))




def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print("Oh no! Player {} just lost {} point(s).".format(who, last_score-score))
        return announce_losses(who, score)
    return say




def pig_latin_original(w):
    """Return the Pig Latin equivalent of a lowercase English word w."""
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin_original(rest(w) + first(w))

def first(s):
    """Returns the first character of a string."""
    return s[0]

def rest(s):
    """Returns all but the first character of a string."""
    return s[1:]

def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    c = first(w)
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

def pig_latin(w):
    """Return the Pig Latin equivalent of a lowercase English word w.
    Use only the first, rest, and starts_with_a_vowel functions to access the contents of a word, 
    and use the built-in len function to determine its length. Do not use any loops.

    >>> pig_latin('pun')
    'unpay'
    >>> pig_latin('sphynx')
    'sphynxay'
    """
    "*** YOUR CODE HERE ***"
    return helper(w, 0)
    
def helper(w, count):
    if starts_with_a_vowel(w) or count == len(w):
        return w + 'ay'
    else:
        return helper(rest(w)+ first(w), count+1)



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    return helper_ten_pairs([int(i) for i in str(n)], 0)

def helper_ten_pairs(lis, count):
    if len(lis) == 0:
        return count
    elif (10-lis[0]) in lis[1:]:
        return helper_ten_pairs(lis[1:], count + lis[1:].count(10-lis[0]))
    else:
        return helper_ten_pairs(lis[1:], count)