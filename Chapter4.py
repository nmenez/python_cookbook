def Chapter4_2():
    print('delegating iteration')

    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node{!r}'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    print(root)
    for ch in root:
        print(ch)


def Chapter4_3():
    print('Creating new iteration patterns with generators')

    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    for n in frange(0, 4, 0.5):
        print(n)


def Chapter4_4():
    print('Implementing the Iterator Protocol')

    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node{!r}'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                yield from c.depth_first()

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)


def Chapter4_5():
    print("iterating in Reverse")
    a = [1, 2, 3, 4, 5]
    for x in reversed(a):
        print(x)


def Chapter4_6():
    """Defining Generator Functions with Extra State
    Problem:
        YOu would like to define a generator function, but it involves extra
        state that you would like to expose to the user somehow
    """
    from collections import deque

    class linehistory:
        def __init__(self, lines, histlen=3):
            self.lines = lines
            self.history = deque(maxlen=histlen)

        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):
                self.history.append((lineno, line))
                yield line

        def clear(self):
            self.history.clear()

    with open('Chapter3.py', 'r') as f:
        lines = linehistory(f)
        for line in lines:
            if 'Decimal' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')


def Chapter4_7():
    """ Problem:
        you want to take a slice o data produced by an iterator, but the
        normal slicing operator doesn't work

        Solution: use itertools islice
    """

    import itertools

    def count(n):
        while True:
            yield n
            n += 1

    c = count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)


def Chapter4_8():
    """ Problem:
        You want to iterate over items in an iterable, but the first few
        items aren't of interest and you just want to discard them

        Solution:
        use iterttols.dropwhile() if you want to skip based on some criteria
        use islice if you know how many items to skip
    """
    from itertools import dropwhile
    with open('test.text') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')


def Chapter4_9():
    """ Iterating over combinations and permutations
        Problem:
        You want to iterate over all of the possible combinations or
        permutations of a collection of items

        Solution: use iterttols.permutations, itertools.combinations,
        itertools.combinations_with_replacement
    """

    items = ['a', 'b', 'c']
    from itertools import permutations
    for p in permutations(items):
        print(p)

    for p in permutations(items, 2):
        print(p)

    from itertools import combinations
    for c in combinations(items, 3):
        print(c)

    for c in combinations(items, 2):
        print(c)

    for c in combinations(items, 1):
        print(c)

    from itertools import combinations_with_replacement
    for c in combinations_with_replacement(items, 3):
        print(c)


def Chapter4_10():
    """ Iterating over the index-value pairs of a sequence
        Problem:
        You want to iterate over a sequence, but would like to keep
        track of which element of the sequence is currently being
        processed

        Solution:
        enumerate() handles this nicely
    """

    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)


def Chapter4_11():
    """ Itearting over Multiple Sequences Simultaneously
    Problem:
    You want to iterate over the items contained
    in more than one sequence at a time
    Solution:
    use zip, or itertools.zip_longest

    """

    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]

    for x, y in zip(xpts, ypts):
        print(x, y)

    ypts = [101, 78, 37, 15, 62, 99, 205]
    from itertools import zip_longest
    for x, y in zip_longest(xpts, ypts):
        print(x, y)

    for x, y in zip_longest(xpts, ypts, fillvalue=0):
        print(x, y)


def Chapter4_12():
    """ Iterating on Items in Separate Containers
    Problem: YOu need to perform the operation on many objects,
    but the objects are contained in  different containers and you would
    like to avoid nested loops without losing the readability of your code
    Solution:
    use itertools.chain
    """

    from itertools import chain
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)


def Chapter4_14():
    """ Flattening a Nested Sequence
    Problem: YOu have a nested sequence that you want to
    flatten into a single list of values
    Solution: write a recursive generator function involving a yield from
    statement

    """

    from collections import Iterable

    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x, ignore_types)
            else:
                yield x
    
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    flat = list(flatten(items))
    print(flat)

def Chapter4_15():
    """ Iterating in Sorted Order Over Merged Sorted Iterables
    PRoblem: 
    you have a collection of sorted sequences and you want to iterate
    over a sorted sequence of them all merged together

    Solution:
    the heapq.merge function works for this
    """

    import heapq
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)

def Chapter4_16():
    """ Replacing Infinite while loops with an iterator
    Problem: You have code that uses a while loop to iteratively
    process data because it involves a function or some kind of
    unusual test condition that doesn't fall into the usual 
    iteration pattern

    Solution:
    use iter()
    """
    pass

if __name__ == "__main__":
    # Chapter4_2()
    # Chapter4_3()
    # Chapter4_4()
    # Chapter4_5()
    # Chapter4_6()
    # Chapter4_7()
    # Chapter4_8()
    # Chapter4_9()
    # Chapter4_10()
    # Chapter4_11()
    # Chapter4_12()
    # Chapter4_14()
    Chapter4_15()
