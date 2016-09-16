# 1.1

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

# 1.2 Unpacking Elements form Iterables of Arbitrary Length
print('\n\n1.2 Unpacking Elements form Iterables of Arbitrary Length')

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


print(drop_first_last((12, 10, 8, 7, 9)))
print(drop_first_last((12, 10, 7, 9)))


# 1.3 Keeping the Last N items
print('\n\n1.3 Keeping the Last N items')
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
    previous_lines.append(line)

with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for plines in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)

# 1.3a
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# 1.4 FInding the Largest or Smallest N Items
print('''\n\n1.4 FInding the Largest or Smallest N Items''')
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

items = [(letter, number)
         for letter, number in zip('abcdefghijklmnopqrstuv', nums)]
print(heapq.nlargest(3, items, key=lambda x: x[1]))
print(heapq.nsmallest(3, items, key=lambda x: x[1]))


# 1.5 implementing a priority queue
print('\n\n1.5 Implementing a priority queue')
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())

# 1.6 Mapping Keys to Multiple Values in  Dictionary
print('\n\n1.6 Mapping Keys to Multiple Values in  Dictionary')

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)
print(d)

# 1.7 Keeping Dictionaries in Order
print('1.7 Keeping Dictionaries in Order')
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key, item, in d.items():
    print(key, item)

# 1.8 Calculating with Dictionaries
print('\n\n1.8 Calculating with Dictionaries' )
prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75
          }

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 1.9 Finding Commonalities in Two Dictionaries
print('''\n\n1.9 Finding Commonalities in Two Dictionaries''')
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

common = a.keys() & b.keys()
print(common)
diff = a.keys() - b.keys()
print(diff)

common_pairs = a.items() & b.items()
print(common_pairs)

# 1.10 removing duplicates from a sequence while maintaining order
print('\n\n1.10 removing duplicates from a sequence while maintaining order')

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print('key x and y')
print(list(dedupe2(a, key=lambda d: (d['x'], d['y']))))
print('\nkey x')
print(list(dedupe2(a, key=lambda d: d['x'])))


# 1.11 Naming a Slice
print('\n\n1.11 Naming a Slice')
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

# 1.11a mapping slice to fit bounds
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])

# 1.12 Determining the Most Frequently Occurring Items in a Sequence
print('\n\n 1.12 Determining the Most Frequently Occurring Items in a Sequence')
from collections import Counter
words = '''look into my eyes look into my eyes the eyes the eyes
the eyes the eyes not around the eyes "dont't" look around the eyes
look into my eyes you're under '''
words = words.replace('\n', '').split(' ')
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = 'why are you not looking in my eyes'.split(' ')
word_counts.update(morewords)
print(word_counts.most_common(3))

print('counters can be added and subracted')
a = Counter(words)
b = Counter(morewords)
print('a', a)
print('b', b)
print('\nadd')
print(a + b)
print('\n subract')
print(a - b)

# 1.13 Sorting a list of dictionaries by a common key
print('''\n\n1.13 Sorting a list of dictionaries by a common key''')
rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 10002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print('\nsorted by fname')
print(rows_by_fname)
print('\nsorted by uid')
print(rows_by_uid)

# equivalent
print('\n using lambda instead of itemgetter')
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=lambda r: r['uid'])

print(rows_by_fname)
print('\n')
print(rows_by_uid)


# 1.14 Sorting Objects without Native Comparison Support
print('\n\n1.14 Sorting Objects without Native Comparison Support')
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'Users({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print('using lambda')
print(sorted(users, key=lambda u: u.user_id))
print('using attrgetter')
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

# 1.15 Grouping Records Together Based on a Field
print('\n\n1.15 Grouping Records Together Based on a Field')
rows = [{'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILL', 'date': '07/04/2012'}]

from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# 1.16 Filtering Sequence Elements
print('\n\n 1.16 Filtering Sequence Elements')
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

print('using generator, more efficient for large lists')
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

print("if filtering criterea cant be expressed easily in list or generator expression")
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

# 1.17 Extracting a Subset of a Dictionary
print('\n\n')
print('1.17 Extracting a Subset of a Dictionary')
# dictionary of all prices over 200
prices = {'ACME': 45.23, 'AAPL': 612.78,
          'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# 1.18 Mapping Names to Sequence Elements
print('\n\n 1.18 Mapping Names to Sequence Elements')
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
addr, joined = sub
print(addr)
print(joined)

new_sub = sub._replace(joined='2014-1,1')
print(new_sub)

# 1.19 Transforming and Reducing Data at the Same Time
print('\n\n 1.19 Transforming and Reducing Data at the Same Time')
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# 1.20 Combining Multipe Mappings into a Single Mapping
print('\n\n  1.20 Combining Multipe Mappings into a Single Mapping')
print('Chainmap takes multiple mapping and makes them logically appear as one')
from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

