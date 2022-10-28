from datetime import datetime,timedelta

today = datetime.today()
next_week = today + timedelta(hours=2)


print(next_week)