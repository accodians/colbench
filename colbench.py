import math
from datetime import datetime
startTime = datetime.now()
s = 1
record = 0
while True:
    s = s + 1
    n = s
    i = 0
    while not n == 1:
        if n % 2 == 0:
            n = n / 2
            i = i + 1
        else:
            n = n * 3 + 1
            i = i + 1
    if i > record:
        record = i
        print (s)
    if s == 2298025:
        print("benchmark finished in", datetime.now() - startTime)
        quit()
