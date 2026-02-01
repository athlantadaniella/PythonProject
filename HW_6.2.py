seconds = int(input('Enter number: '))

while seconds <0 or seconds >= 8640000:
    print('Number must be >=0 and < 8640000')
    seconds = int(input('Enter number: '))

days = seconds // 86400
seconds_remains = seconds % 86400

hours = seconds_remains // 3600
seconds_remains = seconds_remains % 3600

minutes = seconds_remains // 60
seconds_remains = seconds_remains % 60

if 11 <= days % 100 <= 14:
    day_word = 'днів'
else:
    last_digit = days % 10
    if last_digit == 1:
        day_word = 'день'
    elif 2 <= last_digit <= 4:
        day_word = 'дні'
    else:
        day_word = 'днів'

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds_remains).zfill(2)}")