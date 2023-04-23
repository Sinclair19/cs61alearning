def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif x > y:
        return []
    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + path for path in a + b]
    
def merge(s1, s2):
    """ Merges two sorted lists """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])
def mergesort(seq):
    '''
    >>> mergesort([6,4,2,1,4,3,7])
    [1, 2, 3, 4, 4, 6, 7]
    '''
    if len(seq) <= 1:
        return seq
    else:
        return merge(mergesort(seq[:len(seq)//2]), mergesort(seq[len(seq)//2:]))

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'   

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    
    def is_leaf(self):
        return not self.branches

def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    # >>> for path in long_paths(whole, 2):
    # ... print(path)
    # ...
    # <0 1 2>
    # <0 1 3 4>
    # <0 1 3 4>
    # <0 1 3 5>
    # <0 6 7 8>
    # <0 6 9>
    # # <0 11 12 13 14>
    # >>> for path in long_paths(whole, 3):
    # ... print(path)
    # ...
    # <0 1 3 4>
    # <0 1 3 4>
    # <0 1 3 5>
    # <0 6 7 8>
    # <0 11 12 13 14>
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> long_paths(whole, 3)
    [Link(0, Link(1, Link(3, Link(4)))), Link(0, Link(1, Link(3, Link(4)))), Link(0, Link(1, Link(3, Link(5)))), Link(0, Link(6, Link(7, Link(8)))), Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    path_list = []
    if tree.is_leaf() and n <= 0:
        path_list.append(Link(tree.label))
    for branch in tree.branches:
        for path in long_paths(branch, n - 1):
            path_list.append(Link(tree.label, path))
    return path_list

def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ... Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)

class Emotion:
    num = 0
    def __init__(self):
        Emotion.num += 1

    def feeling(self, other):
        if self.power == other.power:
            print('Together')
        elif self.power < other.power:
            other.catchphrase()
            self.catchphrase()
        else:
            self.catchphrase()
            other.catchphrase()


class Joy(Emotion):
    power = 5
    def catchphrase(self):
        print('Think positive thoughts')

class Sadness(Emotion):
    power = 5
    def catchphrase(self):
        print('I\'m positive you will get lost')


def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if lnk == Link.empty or lnk.rest == Link.empty:
        return
    if lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
    else:
        remove_duplicates(lnk.rest)

def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in
    ... zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        yield g
        g = (lambda y: lambda x: f(y(x)))(g)

from operator import add, mul
def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    total = next(it)
    yield total
    for elemnet in it:
        total = f(total, elemnet)
        yield total
