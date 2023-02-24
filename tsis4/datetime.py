import datetime
'''
#problem 1
a = datetime.date.today()
b = datetime.timedelta(days = 5)
print(a - b)
'''
'''
#problem 2
a = datetime.date.today()
b = datetime.timedelta(days = 1)
print("Yesterday:", a - b)
print("Today:", a)
print("Tomorrow:", a + b)
'''
'''
# problem 3
today = datetime.datetime.now()
today = str(today)
x = today.split('.')
print(x[0])
'''
# problem 4
'''
import random
a = random.randint(1, 31)
x = datetime.datetime.now()
y = datetime.datetime.now() - datetime.timedelta(days = a)
b = x - y
print(b.total_seconds())
'''