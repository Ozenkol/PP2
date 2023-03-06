import math as m
import time as t


def square_with_delay(num, time):
    t.sleep(time/1000)
    return m.sqrt(num)


num = int(input())
time = int(input())
print(square_with_delay(num, time))

