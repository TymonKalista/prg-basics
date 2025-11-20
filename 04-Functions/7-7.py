def f(binary):
    if set(binary) == {'0', '1'} or set(binary) == {'1'} or set(binary) =={'0'}:
        return True
    else:
        return False
    
print(f("11"))