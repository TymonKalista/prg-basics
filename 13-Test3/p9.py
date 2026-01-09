def f(uid):
    x = set(uid)
    if len(x)<len(uid):
        return False
    else:
        return True
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))