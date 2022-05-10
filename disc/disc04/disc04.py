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
    que = [0] * (n + 1)
    que[0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                que[i] += que[i - j]
    return que[n]

# WWPD
'''
>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])
1 3
>>> len(a)
5
>>> 2 in a
False
>>> 4 in a
True
>>> a[3][0]
2
'''

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s) - 1) if i % 2 == 0]

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    n = len(s)
    def dfs(i, status):
        if i >= n:
            return 1
        elif status:
            return dfs(i + 1, False)
        else:
            return max(dfs(i + 1, True) * s[i], dfs(i + 1, False))
    return dfs(0, False)

def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n // 10 == 0:
        return True
    return ((n // 10 % 10) < (n % 10)) and ((n // 10 % 10) < (n // 100 %10)) and check_hole_number(n // 100)

def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(n, status):
        if not n // 10:
            return True
        if status and n % 10 < ((n // 10) % 10):
            return helper(n // 10, status)
        return (n % 10) > ((n // 10) % 10) and helper(n // 10, False)
    return helper(n, True)


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)