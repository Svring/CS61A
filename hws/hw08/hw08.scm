(define (rle s)
  (define (helper s pre num)
    (if (or (null? s) (not (= (car s) pre))) (list pre num) (helper (cdr-stream s) pre (+ num 1)))
  )
  (define (next s cur)
    (if (null? s) nil (if (= (car s) cur) (next (cdr-stream s) cur) s))
  )
  (if (null? s) nil (cons-stream (helper (cdr-stream s) (car s) 1) (rle (next s (car s)))))
)


(define (group-by-nondecreasing s)
  (define (helper s now pre)
    (if (and (not (null? s)) (<= pre (car s))) (helper (cdr-stream s) (append now (list (car s))) (car s)) now)
  )
  (define (next s cur)
    (if (null? s) nil (if (>= (car s) cur) (next (cdr-stream s) (car s)) s))
  )
  (if (null? s) nil (cons-stream (helper (cdr-stream s) (list (car s)) (car s)) (group-by-nondecreasing (next s (car s)))))
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

