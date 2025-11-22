def amount_of_words(text):
    x = text.count(' ')
    return x +1
def long_to_sort(text):
    a = text.split()
    b = sorted(a, key=len, reverse=True)
    return b
def alphabet(text):
    a = text.split()
    a.sort()
    return a
print(alphabet('ala ma kota'))