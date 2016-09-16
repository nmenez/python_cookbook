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
    child1 =Node(1)
    child2 =  Node(2)
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
            self._children =[]

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

if __name__ == "__main__":
    # Chapter4_2()
    # Chapter4_3()
    # Chapter4_4()
    Chapter4_5()
