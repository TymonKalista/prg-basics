def f(word):
    word = word.lower()
    word1 = ''
    for char in word:
        word1 = word1 +  '-' + word
    word1 = word1[1::]
    words = []
    words = word1.split('-')
    i = 0
    for element in words:
        element[i].upper()
        i = i +1
    return words
print(f('MONK'))