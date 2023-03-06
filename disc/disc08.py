class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2
    
class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret

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


def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    '''
    if lnk == Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)
    '''
    sum = 0
    while lnk != Link.empty:
        sum += lnk.first
        lnk = lnk.rest
    return sum

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    product = 1
    for lst in lst_of_lnks:
        if lst == Link.empty:
            return Link.empty
        product *= lst.first
    link_lists = [lst.rest for lst in lst_of_lnks]
    return Link(product, multiply_lnks(link_lists))

def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk.rest == Link.empty:
        return
    lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
    flip_two(lnk.rest.rest)

def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    # this doctest don't work
    # use python3 -i disc08.py to manual test
    while link != Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label += 1
    for branch in t.branches:
        make_even(branch)

def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t) # Tree(1, [Tree(4, [Tree(9)]), Tree(16), Tree(25)])
    >>> t.branches[0].branches[0].label
    9
    """
    t.label *= t.label
    for branch in t.branches:
        square_tree(branch)

def find_paths(t, entry):
    '''
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    '''
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for branch in t.branches:
        for path in find_paths(branch, entry):
            paths += [[t.label] + path]
    return paths

def combine_tree(t1, t2, combiner):
    """
    >>> from operator import mul #fix mul not defined
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    templist = []
    for branch1, branch2 in zip(t1.branches, t2.branches):
        templist.append(combine_tree(branch1, branch2, combiner))
    return Tree(combiner(t1.label, t2.label), templist)

def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> t2 = alt_tree_map(t, negate) # should be Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    >>> t2.label
    -1
    >>> t2.branches[0].label
    2
    >>> t2.branches[0].branches[0].label
    -3
    >>> t2.branches[1].label
    4
    """
    def inner(t, depth):
        if depth % 2 == 0:
            label = map_fn(t.label)
        else:
            label = t.label
        return Tree(label, [inner(branch, depth + 1) for branch in t.branches])
    return inner(t, 0)