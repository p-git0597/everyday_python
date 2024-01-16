import time
from datetime import datetime

current_time_1 = datetime.now().strftime('%H:%M:%S')
current_time = (time.strftime('%H:%M:%S'))
print(current_time)
print(current_time_1)

if current_time < '12:00:00':
    print(f"Good Morning Sir")
elif '12:00:00' > current_time < '18:00:00':
    print(f"Good Afternoon Sir")
elif '18:00:00' > current_time < '22:00:00':
    print(f"Good Evening Sir")
else:
    print(f"Good Night Sir")