import json
movie = {
    'Title': 'Click',
    'Main Actor': 'Adam Sandler',
    'Critically Acclaimed': False,
    'Year': 2006,
    'Genre': 'Comedy'
}

file_name ='ClickGoated.json'

with open (file_name, 'w') as file:
    json.dump(movie, file)