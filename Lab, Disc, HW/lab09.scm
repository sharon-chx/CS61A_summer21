(define (over-or-under num1 num2) 
    (cond ((< num1 num2) -1)
          ((= num1 num2) 0)
          (else 1)
    )
)



; ;; Tests
(expect (over-or-under 1 2) -1)

(expect (over-or-under 2 1) 1)

(expect (over-or-under 1 1) 0)

(expect (over-or-under -10 10) -1)

(expect (over-or-under 5 4) 1)

(define (sum-of-squares x y) 
    (+ (* x x)
        (* y y)
    )
)

; ;; Tests
(expect (sum-of-squares 3 4) 25)

(expect (sum-of-squares -1 0) 1)

(expect (sum-of-squares 1 -100) 10001)

(define (make-adder num) 
    (lambda (x) (+ x num))
)

; ;; Tests
(define adder (make-adder 5))

(expect (adder 8) 13)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define lst 
    (cons (cons 1 nil) 
          (cons 2 
                (cons (cons 3 (cos 4 nil)) 
                      (cons 5 nil))))
)

(define (remove item lst) 
    (cond ((null? lst) '())
          (else (filter (lambda (x) (not(= x item))) lst))
    )
    
)

; ;; Tests
(expect (remove 3 nil) ())

(expect (remove 3 '(1 3 5)) (1 5))

(expect (remove 5 '(5 3 5 5 1 4 5 4)) (3 1 4 4))
