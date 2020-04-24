from queue import LifoQueue
stack = LifoQueue(maxsize= 10)
print(stack.join('12'))
for i in range(0, 9):
    stack.put(i)
while stack.empty() is False:
    x = stack.get()
    print(x)
