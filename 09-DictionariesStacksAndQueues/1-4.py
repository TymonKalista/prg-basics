person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

person['surname'] = 'Nowak'
person['married'] = False
person['hobby'].append('bicycle')
person['gender'] = 'Male'
person['phone']['work'] = '313131444'
for key,value in person.items():
   print(f"{key} : {value}")