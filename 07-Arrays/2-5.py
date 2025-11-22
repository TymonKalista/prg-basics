# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = len(cinema_seats[0])*len(cinema_seats)
   return total


def seats_available(seats):
   a_counter = 0
   for row in cinema_seats:
      for item in row:
         if item == 'A':
            a_counter = a_counter +1   
   return a_counter

def seats_booked(seats):
   b_counter = 0
   for row in cinema_seats:
      for item in row:
         if item == 'B':
            b_counter = b_counter +1   
   return b_counter

def seat_status(seats, row, place):
   if seats[row][place] == 'A':
      return 'Available'
   else:
      return 'Booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:',seat_status(cinema_seats,0,0))
print('Seat in row 5, place 5:',seat_status(cinema_seats,4,4))
print('Seat in row 3, place 5:',seat_status(cinema_seats,2,4))