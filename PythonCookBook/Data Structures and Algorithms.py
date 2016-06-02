import heapq
from collections import deque


# If there is a mismatch in the number of elements, you get an error.

p = (4, 5)
x, y = p
# print(x)
# print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
# print(name)
# print(date)

name, shares, price, (year, mon, day) = data
# print(name)
# print(year)
# print(mon)
# print(day)


# Unpacking works with any object that happens to be iterable

s = 'Hello'
a, b, c, d, e = s
# print(a)
# print(b)
# print(e)


# When unpacking, you are able to discard certain values.
# Python has no special syntax for this, but you can often just pick a throwaway variable name for it

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

# print(shares)
# print(price)

# However, make sure that the variable name you pick isn’t being used for something else already.


# It’s worth noting that the phone_numbers variable will always be a list.

record = ('Dave', 'dave@example.com', '555-444-1234', '432-678-3213', '554-456-1929')
name, email, *phone_numbers = record
# print(name)
# print(email)
# print(phone_numbers)


# The starred variable can also be the first one in the list


*trailling, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailling)
print(current)


# Extended iterable unpacking is tailor-made for unpacking iterables of unknown or arbitrary length

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# Keeping the Last N Items


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)



