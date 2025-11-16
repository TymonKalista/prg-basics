def time_string(hours, minutes, time_format):
        result = ' '
        
        if time_format == '24':
              if hours >= 12:
                    result = (f'{hours}:{minutes:02d}')
              else:
                result = (f'0{hours}:{minutes:02d}')
        if time_format == '12':
                if  hours < 12 and hours > 0:
                      result = (f'{hours}:{minutes:02d}am')
                if hours > 12:
                     result = ((f'{hours-12}:{minutes:02d}pm'))
                if hours == 0:
                      result = (f'12:{minutes:02d}am')
                if hours == 12:
                     result = (f'12:{minutes:02d}pm')

        return result

print(time_string(15, 38, '24'))
print(time_string(15, 38, '24') )
print(time_string(8, 3, '24')) 
print(time_string(0, 5, '24') )
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12')) 
print(time_string(12, 46, '12')) 
print(time_string(13, 10, '12')) 
print(time_string(19, 2, '12'))






