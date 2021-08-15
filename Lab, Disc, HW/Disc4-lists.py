def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    maxnum = 0
    if not s:
        return 1
    else:
        return max(s[0]*max_product(s[2:]), max_product(s[1:]))




def closest_number(nums, target):
    """
    >>> closest_number([1, 4, 5, 6, 7], 2)
    1
    >>> closest_number([3, 1, 5, 6, 13], 4) #  choose the earlier number since there's a tie
    3
    >>> closest_number([34, 102, 8, 5, 23], 25)
    23
    """
    return min(nums, key=lambda x: abs(target - x))



def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for i in s:
        key = fn(i)
        if key in grouped:
            grouped[key].append(i)
        else:
            grouped[key] = [i]
    return grouped




def subset_sum(target, lst):
    """Returns True if it is possible to add some of the integers in lst
    to get target.

    >>> subset_sum(10, [-1, 5, 4, 6])
    True
    >>> subset_sum(4, [5, -2, 12])
    False
    >>> subset_sum(-3, [5, -2, 2, -2, 1])
    True
    >>> subset_sum(0, [-1, -3, 15])     # Sum up none of the numbers to get 0
    True
    """
    if target == 0:
        return True
    elif target !=0 and not lst:
        return False
    else:
        #two ways of examination, use the first element for calcuation or now, as long as one of those methods works, it returns True
        a = subset_sum(target - lst[0], lst[1:])
        b = subset_sum(target, lst[1:])
        return a or b



def intersection(lst_of_lsts):
    """Returns a list of elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    """
    elements = []
    for num in lst_of_lsts[0]:
        condition = True
        for lst in lst_of_lsts[1:]:
            if num not in lst:
                condition = False
        if condition:
            elements += [num]
    return elements




def wordify(s):
    """ Takes a string s and divides it into a list of words. Assume that the last element of the string is a whitespace.
    Duplicate words allowed.
    >>> wordify ('sum total of human knowledge ')
    ['sum', 'total', 'of', 'human', 'knowledge']
    >>> wordify ('one should never use exclamation points in writing! ')
    ['one', 'should', 'never', 'use', 'exclamation', 'points', 'in', 'writing!']
    """
    start, end, lst = 0, 0, []
    for letter in s:
        if letter != ' ':
            end = end + 1
        elif start == end :                    #i think this elif is not neccessary
            start, end = start+1,end+1
        else :
            lst += [s[start: end]]
            start, end = end+1, end+1
    return lst