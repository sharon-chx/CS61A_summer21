def if_macro(condition, true_result, false_result):
    """
    >>> eval(if_macro("True", "3", "4"))
    3
    >>> eval(if_macro("0", "'if true'", "'if false'"))
    'if false'
    >>> eval(if_macro("1", "print('true')", "print('false')"))
    true
    >>> eval(if_macro("print('condition')", "print('true_result')", "print('false_result')"))
    condition
    false_result
    """
    "*** YOUR CODE HERE ***"
    return f"{true_result} if {condition} else {false_result}"


def make_lambda(params, body):
    """
    >>> f = eval(make_lambda("x, y", "x + y"))
    >>> f
    <function <lambda>>
    >>> f(1, 2)
    3
    >>> g = eval(make_lambda("a, b, c", "c if a > b else -c"))
    >>> g(1, 2, 3)
    -3
    >>> eval(make_lambda("f, x, y", "f(x, y)"))(f, 1, 2)
    3
    """
    "*** YOUR CODE HERE ***"
    return f"lambda {params}: {body}"



#=====================================================
#below is Scheme code

"""Q8: If Macro Scheme

Using regular define below
scm> (if-function '(= 0 0) '2 '3)
(if (= 0 0) 2 3)
scm> (eval (if-function '(= 0 0) '2 '3))
2
scm> (if-function '(= 1 0) '(print 3) '(print 5))
(if (= 1 0) (print 3) (print 5))
scm> (eval (if-function '(= 1 0) '(print 3) '(print 5)))
5
"""

(define (if-function condition if-true if-false)
  `(if ,condition ,if-true ,if-false)
)


""" Using marco below
scm> (if-macro (= 0 0) 2 3)
2
scm> (if-macro (= 1 0) (print 3) (print 5))
5
"""

(define-macro (if-macro condition if-true if-false)
  `(if ,condition ,if-true ,if-false)
)



"""Q9: Or Macro
takes in two expressions and or's them together (applying short-circuiting rules).
scm> (or-macro (print 'bork) (/ 1 0))
bork
scm> (or-macro (= 1 0) (+ 1 2))
3
"""


(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1 ,expr2))
)


"""Q10: Replicate
Regular define version

scm> (repeat-n (print '(resistance is futile)) 3)
(resistance is futile)
(resistance is futile)
(resistance is futile)

scm> (repeat-n (print (+ 3 3)) (+ 1 1))  ; Pass a call expression in as n
6
6
"""

(define (replicate x n)
    
    (if (> n 0)
        (cons x (replicate x (- n 1)))
        '()
    )
)


(define-macro (repeat-n expr n)

  (cons 'begin (replicate expr (eval n)))
)



"""Q11: When Macro

If the condition is not false (a truthy expression), 
all the subsequent operands are evaluated in order and the value 
of the last expression is returned. Otherwise, the entire when expression evaluates to okay.

scm> (when (= 1 0) ((/ 1 0) 'error))
okay

scm> (when (= 1 1) ((print 6) (print 1) 'a))
6
1
a

"""


(define-macro (when condition exprs)
  `(if ,condition 
    ,(cons 'begin exprs) 
     'okay)
  )


