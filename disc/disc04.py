def count_stair_ways(n):
    if n == 1 or n == 2:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)


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
    dict1 = {}
    def count_k_inner(n,k):
        if n in dict1:
            return dict1[n]
        if n == 1 or n == 0:
            dict1[n] = 1
            return 1
        if n < 0:
            dict1[n] = 0
            return 0
        tmp = 0
        for i in range(1, k + 1):
            tmp += count_k_inner(n - i, k)
        dict1[n] = tmp
        return tmp
    return count_k_inner(n,k)

def even_weighted(s): 
    """
    >>> x = [1, 2, 3, 4, 5, 6] 
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i]*i for i in range(len(s)) if s[i] % 2 == 1]

def max_product(s): 
    """Return the maximum product that can be formed using non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9 
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5 
    125
    >>> max_product([])
    1
    >>> max_product([5,10,5,10,10,5,100,5])
    25000
    """
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    return max(s[0]*max_product(s[2:]), max_product(s[1:]))

def max_product_2(s): 
    """Return the maximum product that can be formed using non-consecutive elements of s.
    
    pass s without slice to save space
    
    >>> max_product_2([10,3,1,9,2]) # 10 * 9 
    90
    >>> max_product_2([5,10,5,10,5]) # 5 * 5 * 5 
    125
    >>> max_product_2([])
    1
    >>> max_product_2([5,10,5,10,10,5,100,5])
    25000
    """
    def max_product_inner(s, begin):
        if begin == len(s):
            return 1
        if begin == len(s) - 1:
            return s[begin]
        return max(s[begin] * max_product_inner(s, begin + 2), max_product_inner(s, begin + 1))
    return max_product_inner(s, 0)
