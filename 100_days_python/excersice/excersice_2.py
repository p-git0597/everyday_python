import time
t= time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if(hour >= 0 and hour < 12):
    print(f"Good morning! It's {hour} in the morning.")
elif(hour >=12 and hour < 17):
    print(f"Hello Good Afternoon! It's {hour}PM in the day.")
elif(hour >=17 and hour < 21):
    print(f"Hello Good Evening! It's {hour}PM in the day.")
else:
    print("It is very late, go to bed. Good Night!")