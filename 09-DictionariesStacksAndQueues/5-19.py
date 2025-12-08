import json
with open('reservations.json', 'r') as file:
    data = json.load(file)
    reservations = data['reservations']


def number_of_rooms():   
    return len(reservations)
print(number_of_rooms())

def number_of_paid_res():
    counter1 = 0
    for item in reservations:
        if item['paid'] == True:
            counter1 = counter1 + 1
    return counter1
print(number_of_paid_res())

def number_of_unpaid_res():
    counter2 = 0
    for item in reservations:
        if item['paid'] == False:
            counter2 = counter2 + 1
    return counter2
print(number_of_unpaid_res())

def value_of_paid():
    counter3 = 0
    for item in reservations:
        if item['paid'] == True:
            counter3= counter3 + item['price_per_night']*item['nights']
    return counter3
print(value_of_paid())

def value_of_paid():
    counter4 = 0
    for item in reservations:
        if item['paid'] == False:
            counter4= counter4 + item['price_per_night']*item['nights']
    return counter4
print(value_of_paid())
