(define (split-at lst n)
  (cond ((eq? n 1) (cons (cons (car lst) nil) (cdr lst)))
        ((eq? n 0) (cons nil lst))
        ((eq? lst nil) (cons lst nil))
        (else (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1))))))
)


(define (compose-all funcs)
  (lambda (x) (cond ((null? funcs) x)
                    (else ((compose-all (cdr funcs)) ((car funcs) x)))))
)

