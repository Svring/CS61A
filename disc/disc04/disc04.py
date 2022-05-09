def multiply(m, n):
    """
    multiply

    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n == 0 or n == 1:
        return False
    return prime_helper(n, 2)
    
def prime_helper(n, m):
    if m == n - 1:
        return True
    if n % m == 0:
        return False
    else:
        return prime_helper(n, m + 1)

def count_stair_ways(n):
    if n <= 2:
        return n
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """

    

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)