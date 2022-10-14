import matplotlib
from numpy import random
import time
#%matplotlib inline
import matplotlib.pyplot as plt
array10 = random.randint(0, 100, 10)
array100 = random.randint(0, 100, 100)
array1000 = random.randint(0, 100, 1000)
array10000 = random.randint(0, 100, 10000)
array100000 = random.randint(0, 100, 100000)
print(array10)
def stopwatch(array):
    timestart = time.time()
    sum(array)
    time1 =  time.time() - timestart
    return time1
print(stopwatch(array10), stopwatch(array100), stopwatch(array1000), stopwatch(array10000), stopwatch(array100000))
plt.plot((10, 100, 1000, 10000, 100000), (stopwatch(array10), stopwatch(array100), stopwatch(array1000), stopwatch(array10000), stopwatch(array100000)))
plt.show()