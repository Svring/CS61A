(define (three n) 
  (cons-stream n (three (+ n 3)))
)

(define f (three 0))

(car f)

(car (cdr-stream f))