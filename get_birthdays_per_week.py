from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    weekday = {'Monday': [],
               'Tuesday': [],
               'Wednesday': [],
               'Thursday': [],
               'Friday': [],
               }
    current_time = datetime.now().date()

    for i in range(1,8):
        interval = current_time + timedelta(days=i)
        for d in users:
            if interval == datetime(year=current_time.year, month=d['birthday'].month, day=d['birthday'].day).date():
                if (interval.strftime('%A') == 'Saturday' or interval.strftime('%A') == 'Sunday'):
                    weekday['Monday'].append(d['name'])
                else:
                    day = interval.strftime('%A')
                    weekday[day].append(d['name'])

    return weekday


users = [{'name': 'Bill','birthday': datetime(year=1980, day=25, month=5)},
         {'name': 'Jim','birthday': datetime(year=1979, day=19, month=5)},
         {'name': 'Kim','birthday': datetime(year=1974, day=19, month=5)},
         {'name': 'Jam','birthday': datetime(year=1985, day=21, month=5)},
         {'name': 'Peter','birthday': datetime(year=1993, day=25, month=5)}
         ]

print(get_birthdays_per_week(users))