def f(password):
    if len(password) <6:
        return False
    if len(set(password)) < len(password):
        return False
    else:
        return True
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))