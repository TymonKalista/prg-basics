###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7 and 10 > month:
    quarter = 3
elif month >= 4 and 7 > month:
    quarter = 2
elif month >= 0 and 4 > month:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')