(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (
    car (cdr s)
  )
)

(define (caddr s)
  (
    car (cddr s)
  )
)


(define (sign num)
  (cond ((= num 0) 0) ((> num 0) 1) (else -1))
)

(define (square x) (* x x))

(define (pow x y)
  (if (= y 1) x
    (
      if (even? y)
      (square (pow x (/ y 2)))
      (* x (square (pow x (floor (/ y 2)))))
    )
  )
)


(define (unique s)
  (
    if (null? s) nil
    (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) s)))
  )
)


(define (replicate x n)
  (define (helper x n s)
    (
      if (= n 0) s
      (helper x (- n 1) (cons x s))
    )
  )
  (helper x n nil)
)


(define (accumulate combiner start n term)
  (
    define (helper f n)
    (if (= n 1) (term n) (combiner (f n) (helper f (- n 1))))
  )
  (combiner start (helper term n))
)


(define (accumulate-tail combiner start n term)
  (
    if (= n 1) (combiner start (term n))
    (accumulate-tail combiner (combiner start (term n)) (- n 1) term)
  )
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)