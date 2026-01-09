import re
def f(mnumbers):
    pattern = '^[+-]?[1-7A-Da-d]+$'
    j = 0
    for i in mnumbers:
        if re.fullmatch(pattern,i):
            j = j +1
    return j
print(f(["A15","-31","7abC","+D1","-g4"]))
