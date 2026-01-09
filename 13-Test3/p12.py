import re
def f(dates):
    dates_group = dates.split(',')
    new_dates = []
    pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    for elem in dates_group:
        if re.fullmatch(pattern, elem):
            new_dates.append(elem)
    return new_dates
print(f("2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"))