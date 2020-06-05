from collections import deque

# Lists as Stack
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append("Mango")
print(fruits)
fruits.pop()
print(fruits)

# Lists as Queues

queue = deque(['orange', 'apple', 'pear', 'banana'])
print(queue)
queue.append('mango')
print("After appending to right of list: {}".format(queue))
queue.popleft()
print("After remobing from left of list: {}".format(queue))
queue.pop()
print("After remobing from right of list: {}".format(queue))

# Dictionary

d = {}  # or d = dict()

d['first'] = 'orange'
d['second'] = 'grapes'
d[3] = 'kiwi'
print(d)
print(d.keys())
print(d.values())

for i in d:
    print(str(i) + " : " + d[i])

for index, value in enumerate(d):
    print(index, value, d[value])


# tuples


tup1 = (0, 1, 2, 3, 4)
tup2 = ('apple', 'orange')

# Concatenating above two
tup3 = tup1 + tup2
print(tup3)

# create a tuple with repetition
repTuple = ("python",)*3
print(repTuple)

# converting a list into tuple

list1 = [0, 1, 2]
print(tuple(list1))


# sets

people = {"Jay", "Idrish", "Archi"}
print("People: {}".format(people))
people.add("Daxit")
print("People: {}".format(people))

for i in range(1, 6):
    people.add(i)

print("People: {}".format(people))

set1 = set()
for i in range(1, 5):
    set1.add(i)

set2 = set()
for i in range(3, 7):
    set2.add(i)


print(set1 | set2)  # sets are merged
print(set1 & set2)  # Common Elements are selected
print(set1 - set2)  # Difference of two sets
