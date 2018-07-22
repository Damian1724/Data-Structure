/*
Author:Damian Cruz
*/


import time
import random
my_randoms=[]
cola=MyQueue()
timing=[]
for j in range(200):
    for i in range(10000):
        my_randoms.append(random.randrange(1,1000000000000,2))
    start=time.clock()
    for i in my_randoms:
        cola.enqueue(i)
    for i in range(len(my_randoms)):
        cola.dequeue()
    end=time.clock()
    timing.append(end-start)
    my_randoms.clear()
n=0
for i in timing:
    n+=i
average=n/200
print("The average time is {}".format(average))
sorted(timing)
print("The median is {}".format((timing[99]+timing[100])/2))
for i in timing:
    n+=(i-average)**2
print("The varience is {}".format(n/199))
