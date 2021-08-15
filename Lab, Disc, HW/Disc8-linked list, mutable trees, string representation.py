class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
    
def sum_nums(s):
    """
    a function that takes in a linked list and returns the sum of all its elements.
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    # method 1: while loop:
    total = 0
    while s.rest is not Link.empty:
        total += s.first
        s = s.rest
    return total + s.first

    # method 2: recursion
    if s.rest is Link.empty:
        return s.first
    return s.first + sum_nums(s.rest)



def multiply_lnks(lst_of_lnks):
    """
    a function that takes in a Python list of linked lists and multiplies them element-wise. 
    It should return a new linked list.
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    if len(lst_of_lnks) == 0:
        return Link.empty
    else:
        total = 1
        lnks_rest = []
        for item in lst_of_lnks:
            total *= item.first
            if item.rest is not Link.empty:
                lnks_rest.append(item.rest)
        if len(lnks_rest)<len(lst_of_lnks):
            lnks_rest = []
        return Link(total, multiply_lnks(lnks_rest))



def flip_two(s):
    """
    Takes as input a linked list s and mutates s so that every pair is flipped.
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    if s.rest is not Link.empty and s is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        s = s.rest.rest
        flip_two(s)




class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


def make_even(t):
    """
    Takes in a tree t whose values are integers, and mutates the tree such that 
    all the odd integers are increased by 1 and all the even integers remain the same.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.label % 2 == 1:
        t.label += 1
    for branch in t.branches:
        make_even(branch)


def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    result = []
    if t.is_leaf():
        result.append(t.label)
    else:
        for branch in t.branches:
            result += leaves(branch)
    return result



def find_paths(t, entry):
    """
    given a Tree t and an entry, returns a list of lists containing the nodes 
    along each path from the root of t to entry.
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for branch in t.branches:
        for path in find_paths(branch, entry):
            paths.append([t.label] + path)
    return paths


