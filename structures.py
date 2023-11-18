from array import array
from collections import deque

numbers = array('i', [1, 2, 3, 4, 5])
print(numbers)
print(len(numbers))

for number in numbers:
    print(number)

print(numbers[:2])

numbers.append(6)
print(numbers)

numbers.extend([7, 8, 9])
print(numbers)

graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}
print(graph[1])

queue = deque(['a', 'b', 'c'])
print(queue)

queue.pop()
print(queue)

queue.popleft()
queue.append('d')
queue.appendleft('e')
print(queue)
