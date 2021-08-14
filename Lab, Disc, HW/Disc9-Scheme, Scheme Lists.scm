
; ;; A function that returns the factorial of a number.
(define (factorial x)
  (if (= x 0) 1 (* x (factorial(- x 1))))
)

(expect (factorial 5) 120)
(expect (factorial 0) 1)



; ;; A function that returns the n-th Fibonacci number.
(define (fib n)
    (if (<= n 2) 1
        (+ (fib(- n 1)) (fib(- n 2)))
    )
)

(expect (fib 10) 55)
(expect (fib 1) 1)



; ;; make the same list with list, quote, and cons.
(define with-list
    (list (list 'a 'b) 'c 'd list('e))
)
(draw with-list)

(define with-quote
    '((a b) c d (e))
)
(draw with-quote)

(define helpful-list
   (cons 'a (cons 'b nil))
)
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil)))
)
(draw another-helpful-list)

(define with-cons
    (cons (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil))))
)
(draw with-cons)



; ;; A function which takes two lists and concatenates them.
(define (list-concat a b)
    (append a b)
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))



; ;; A function that, when given a list, such as (1 2 3 4), duplicates every element in the list (i.e. (1 1 2 2 3 3 4 4)).
(define (duplicate lst)
    (if (null? lst) lst
    	(cons (car lst) (cons (car lst) (duplicate(cdr lst))))
    )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))



; ;; Afunction that, when given an element, a list, and an index, inserts the element 
; ;; into the list at that index. You can assume that the index is in bounds for the list.
(define (insert element lst index)
	(if (= index 0)
	    (cons element lst)
	    (cons (car lst) (insert element (cdr lst) (- index 1)))
	)
)

(expect (insert 2 '(1 7 9) 2) (1 7 2 9))
(expect (insert 'a '(b c) 0) (a b c))
