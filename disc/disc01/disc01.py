def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp <= 60 or raining:
        return True
    else:
        return False
    
    #one-line version: return raining and temp <= 60


def square(x):
    print('here!')
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))

#output:
#Error, function 'so_slow' is infinite loop.


def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


#'About environment diagram, the best way to understand is draw it by yourself'
#'do not forget to see if you are right at https://pythontutor.com/composingprograms.html#mode=edit'


#Proceed with call-tion
'''
(1)print(4, 5) + 1

output:
4, 5
Error

(2)2 * 2 * 1 + x * x

output:
13

(3)print(3 * 3 * 1)

output:
9

(4)print(x + 1 * x + 1)

output:
7

(5)print(print(x + 1 * x + 1))

output:
7
None

(6)print(print(x + 1 * x + 1) + 1)

output:
7
Error

(7)print(p("rint"))

output:
rint
None

(8)x, y = 2, x
   g(y, x)

output:
one
True 2
2
None
Error

(9)g(y, p("rint"))

output:
rint
one
False None
None
None
Error
'''