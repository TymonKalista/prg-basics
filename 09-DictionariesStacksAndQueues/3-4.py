import queue

stack = queue.LifoQueue()

binary = int(input('ENTER YOUR NUMBER: '))

while binary > 0:
    x = binary%2
    stack.put(x)
    binary = binary//2
while not stack.empty():
    print(stack.get(), end='')
