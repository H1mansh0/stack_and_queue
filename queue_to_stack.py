"""
Task2
"""
from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def queue_to_stack(queue):
    """
    Transform stack to queue
    """
    temp = []
    stack = ArrayStack()
    for i in queue:
        temp += [i]
    for i in temp[-1::-1]:
        stack.push(i)
    return stack






queue = ArrayQueue()
for i in range(10):
    queue.add(i)
stack = queue_to_stack(queue)
print(queue)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(stack)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(stack.pop())
# 0
print(queue.pop())
# 0
stack.add(11)
queue.add(11)
print(queue)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(stack)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
