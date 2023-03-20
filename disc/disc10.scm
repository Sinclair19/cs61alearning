((define (factorial x)
    (if (= x 1) 1 (* x (factorial (- x 1))))))

(define (fib n) (cond ((= n 0) 0)
                      ((= n 1) 1)
                      ((= n 2) 1)
                      (else (+ (fib (- n 1)) (fib (- n 2))))))

(define (my-append a b) 
        (if (eq? (cdr a) nil) 
            (cons (car a) b) 
            (cons (car a) (my-append (cdr a) b))))

(car (cdr (cdr (cdr s))))

(define (duplicate lst) 
        (if (null? lst) lst 
            (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))

(define (insert element lst index)
        (if (= index 0) 
            (cons element lst)
            (cons (car lst) (insert element (cdr lst) (- index 1)))))