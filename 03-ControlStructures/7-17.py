time = input("Enter time(24-hour format): ")
actual_time = " "
if time[0:2] == "13":
    actual_time = '1'
elif time[0:2] == "14":
    actual_time = '2'
elif time[0:2] == "15":
    actual_time = '3'
elif time[0:2] == "16":
    actual_time = '4'
elif time[0:2] == "17":
    actual_time = '5'
elif time[0:2] == "18":
    actual_time = '6'
elif time[0:2] == "19":
    actual_time = '7'
elif time[0:2] == "20":
    actual_time = '8'
elif time[0:2] == '21':
    actual_time = '9'
elif time[0:2] == '22':
    actual_time = '10'
elif time[0:2] == '23':
    actual_time = '11'
elif time[0:2] == '24':
    actual_time = ''

else:
    actual_time = time

if time[0:2] == '13' or time[0:2] == '14' or time[0:2] == '15' or time[0:2] == '16' or time[0:2] == '17' or time[0:2] == '18' or time[0:2] == '19' or time[0:2] == '20' or time[0:2] == '21' or time[0:2] == '22' or time[0:2] == '23' or time[0:2] == '24':
    print(f'Time in 12-hour format: {actual_time}{time[2:5]}pm')
else:
    print(f'Time in 12-hour format: {actual_time}am')




 
 
