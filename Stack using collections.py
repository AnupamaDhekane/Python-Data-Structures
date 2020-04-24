from collections import deque
from random import randint

stack = deque()
stack.append("an ass")
for a in range(0, 100):
    stack.append(randint(0, a))
while len(stack) != 0:
    x = stack.pop()
    print(x)
