(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items)
    nil
    (cons (proc (car items))
      (map proc (cdr items)))))

(define (cons-all first rests)
  (define (con rest)
    (cons first rest))
    (map con rests))

(define (zip pairs)
  (let ((first (map (lambda (pair) (car pair)) pairs))

        (rest (map (lambda (pair) (cadr pair)) pairs)))

        (list first rest)))

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (adding_idx i lst)
    (if (null? lst) 
      nil
      (cons (list i (car lst))
        (adding_idx (+ i 1) (cdr lst)))))
  (adding_idx 0 s))
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond
      ((null? denoms) cons nil)
      ((= total 0) cons(cons nil nil))
      ((> (car denoms) total) (list-change total (cdr denoms)))
      (else (append 
    (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
    (list-change total (cdr denoms))))
  ))
  
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
            
            (cons form (cons params (map let-to-lambda (cddr expr))))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (let ((zipped_val (zip values)))

              (let ((para_val (map let-to-lambda (cadr zipped_val)))
                    (func (append (list 'lambda (car zipped_val))
                            (map let-to-lambda body))))
                    (cons func para_val)))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
