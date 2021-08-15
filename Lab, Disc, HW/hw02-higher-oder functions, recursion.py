from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"

    def f(x):
    	if n == 0:
    		return x
    	else:
    		tracker = func(x)
    		for i in range(n-1):
    			tracker = func(tracker)
    		return tracker
    return f



def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 8:
    	return 1
    elif pos < 10 and pos != 8:
    	return 0
    else:
    	return num_eights(pos%10) + num_eights(pos//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    """implement a from-bottom-to-top recursion(indicated by return helper(1, 0, 1)), 
    using a helper fuction."""

    def helper(index, ppn, sign):
    	if n == index:
    		return ppn + sign
    	elif num_eights(index) != 0 or index%8 == 0:
    		return helper(index+1, ppn+sign, -sign)
    	else:
    		return helper(index+1, ppn+sign, sign)
    return helper(1, 0, 1)




def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # base case: if get to the last digit, return count
    # recursively compare last and second to last digit, to find out how many digits missing in between
    def helper(number, last_digit, count):
    	if number == 0:
    		return count
    	elif number == last_digit:
    		return count
    	elif number < 10:
    		return count + last_digit - number - 1
    	elif (last_digit - number%10) > 1:
    		return helper(number//10, number%10, count+(last_digit-number%10-1))
    	else:
    		return helper(number//10, number%10, count)
    return helper(n//10, n%10, 0)

def get_next_coin(coin):
    """Return the next coin. 
    >>> get_next_coin(1)
    5
    >>> get_next_coin(5)
    10
    >>> get_next_coin(10)
    25
    >>> get_next_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)	
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    # tree recursion like the path function in lab3. need helper on using arguments num(=current change amt) and coin used
    # recursion on num after subtracting current coin and skip current coin, use next coin on the num (so that it uses largest coin as possible)
    # count_coins(10) = help(10,1)
    #                     /   \
    #            help(9,1)   help(10, 5)
    #             /  \          /       \
    #    help(8,1)  help(9,5) help(5,5)  help(10,10) #return 2 from last 2 help
    #help(7,1)help(8,5)help(4,5)help(9,10) #return 0 from last 2 help
    def help(num, coin):
    	if not coin:    # when get_next_coin returns None - reached 25 before already         
    		return 0
    	elif num < coin:    # can't be split anymore, but not reach the end, so this is not a valid split
    		return 0
    	elif num == coin:    #reach the end of split
    		return 1
    	else:
    		return help(num-coin, coin)+help(num, get_next_coin(coin))
    return help(change, 1)

