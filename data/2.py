import datetime

date = datetime.datetime.today()
date1 = datetime.datetime.today() - datetime.timedelta(days=1)
date2 = datetime.datetime.today() + datetime.timedelta(days=1)
print(date1)
print(date)
print(date2)