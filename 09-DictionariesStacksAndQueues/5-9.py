dict ={
    'D': 'Dolnośląskie',
    'C': 'Kujawsko-pomorskie',
    'L':'Lubelskie',
    'F':'Lubuskie',
    'E': 'Łódzkie',
    'K': 'Małopolskie',
    'W':'Mazowieckie',
    'O':'Opolskie',
    'R':'Podkarpackie',
    'B':'Podlaskie',
    'G': 'Pomorskie',
    'S':'Śląskie',
    'T': 'Świętokrzyskie',
    'N':'Warmińsko-mazurskie',
    'P': 'Wielkopolskie',
    'Z': 'Zachodniopomorskie'
}
letters = ''
counter = {woj: 0 for woj in dict.values()}
with open('vehicle.txt', 'r') as file:
    for line in file:
        letters  = letters + line[0]
for char in letters:
    if char in dict:
        woj = dict[char]
        counter[woj] += 1

for woj, liczba in counter.items():
    print(f"{woj}: {liczba}")

        
