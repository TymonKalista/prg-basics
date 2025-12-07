import queue
stack = queue.LifoQueue()
def rpn(notation):
     for char in notation:
        if char.isdigit():
            stack.put(int(char))
        if char == '+':
            x = int(stack.get())
            y = int(stack.get())
            z = x + y
            stack.put(z)
        if char == '-':
            x = int(stack.get())
            y = int(stack.get())
            z = x - y
            stack.put(z)
        if char == '*':
            x = int(stack.get())
            y = int(stack.get())
            z = x * y
            stack.put(z)
        if char == '/':
            x = int(stack.get())
            y = int(stack.get())
            z = x / y
            stack.put(z)
        if char == '=':
            z = stack.get()
            print(z)
rpn('8 3 1 + / 3 2 – 4 + * =')
            