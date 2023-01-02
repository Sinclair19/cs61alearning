def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    sum = 1
    while k != 0:
        sum = sum * n
        n -= 1
        k -= 1
    return sum


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    width = len(str(y)) - 1
    sum = 0
    while width >= 0:
        temp = y // 10**width
        sum += temp
        y -= 10**width * temp
        width -= 1
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    width = len(str(n)) - 1
    flag = 0 # if two eights in a row, than it equal 1
    while width >= 0:
        temp = n // 10**width
        n -= 10**width * temp
        width -= 1
        if temp == 8 and (n // 10**width) == 8:
            flag = 1
    if flag == 1:
        return True
    else:
        return False

