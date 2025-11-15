###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
numer = 0

while len(text) > numer:
    char = text[numer]
    if char in vowels:
        vowel_count += 1
        numer += 1
    else:
        numer += 1

print(f"The number of vowels in the text is: {vowel_count}")
