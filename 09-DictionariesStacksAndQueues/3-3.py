import queue

def brackets_ok(expression):
   stack = queue.LifoQueue()
   for i in range(0,len(expression)):
      if expression[i] == '['  or expression[i] == '('  or expression[i] == '{' :
         stack.put(expression[i])
      if expression[i] == ']':
        if stack.empty() or stack.get() != '[':
          return False
      if expression[i] == ')':
            if stack.empty() or stack.get() != '(':
                return False
      if expression[i] == '}':
            if stack.empty() or stack.get() != '{':
                return False
   return stack.empty()



print(brackets_ok("[(2+3)*4+5]/6-{(7*8)+[4]}"))  
print(brackets_ok("[(2+3]/4)"))                  
print(brackets_ok("(2-3*4+(5/6)")) 