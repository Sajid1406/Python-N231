import datetime

my_date = datetime.date(2023,4,20)
print(my_date)

print(my_date.strftime("%A %B %d, %Y"))
print(my_date.weekday())

import datetime
import pytz

my_date = datetime.datetime(2021,3,29,11,52,0,tzinfo=pytz.UTC)
print(my_date)
central_time = pytz.timezone('US/Central')
print(my_date.astimezone(central_time))

import datetime

start = datetime.date(1998,3,29)
end = datetime.date(2023,3,29)
duration = end-start
print(duration.days)

import math

degree = 90
radians = math.radians(degree)
print(radians)
sine = math.sin(radians)
cos = math.cos(radians)
tangent = math.tan(radians)
print(sine,cos,tangent)

import math
x= math.pow(2,3) # 2**3
print(x)

base =10
y = math.log(100,10) # log10(100) -> log10(10^2) ->2.log10(10) -> 2*1 ->2
print(y)

import math

circumference = 2*math.pi*6
print(math.pi)
print(circumference)
area = math.pi*6*6
print(area)

import random

x= random.randint(1,100)
print(x)
y = random.random()
print(y)

import json

person = {"name":"Hello","age":30}
person_json = json.dumps(person)
print(person_json)