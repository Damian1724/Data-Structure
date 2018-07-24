/*
Author:Damian Cruz
*/

# These two methods are for MyQueue

def enqueue_timing():
    import time
    import random
    my_randoms=[]
    cola=MyQueue()
    timing=[]
    for i in range(200):
        for j in range(10000):
            my_randoms.append(random.randrange(1,1000000000000,2))
        start=time.clock()
        for j in my_randoms:
            cola.enqueue(j)
        end = time.clock()
        timing.append(end-start)
        my_randoms.clear() 
    sum_timing=0
    for i in timing:
        sum_timing+=i
    average=sum_timing/200
    print("The average time is {}".format(average))
    sorted(timing)
    median=(timing[99]+timing[100])/2
    print("The median is {}".format(median))
    varience=0
    for i in timing:
        varience+=(i-average)**2
    print("The varience is {}".format(varience/199))
     
def dequeue_timing():
    import time
    import random
    my_randoms=[]
    cola=MyQueue()
    timing=[]
    for i in range(200):
        for j in range(10000):
            my_randoms.append(random.randrange(1,1000000000000,2))
        for j in my_randoms:
            cola.enqueue(j)
        start = time.clock()
        for j in range(len(my_randoms)):
            cola.dequeue()
        end = time.clock()
        timing.append(end-start)
        my_randoms.clear()
    sum_timing=0
    for i in timing:
        sum_timing+=i
    average=sum_timing/200
    print("The average time is {}".format(average))
    sorted(timing)
    median=(timing[99]+timing[100])/2
    print("The median is {}".format(median))
    varience=0
    for i in timing:
        varience+=(i-average)**2
    print("The varience is {}".format(varience/199))

#These two methods are for Myqueue_LinkedList    
    
def enqueue_timing():
    import time
    import random
    my_randoms=[]
    timing=[]
    for i in range(200):
        cola = MyQueue_LinkedList()
        for j in range(10000):
            my_randoms.append(random.randrange(1,1000000000000,2))
        start=time.clock()
        for j in my_randoms:
            cola.enqueue(j)
        end = time.clock()
        timing.append(end-start)
        my_randoms.clear()
    sum_timing=0
    for i in timing:
        sum_timing+=i
    average=sum_timing/200
    print("The average time is {}".format(average))
    sorted(timing)
    median=(timing[99]+timing[100])/2
    print("The median is {}".format(median))
    varience=0
    for i in timing:
        varience+=(i-average)**2
    print("The varience is {}".format(varience/199))
    
 def dequeue_timing():
    import time
    import random
    my_randoms=[]
    timing=[]
    for i in range(200):
        cola=MyQueue_LinkedList()
        for j in range(10000):
            my_randoms.append(random.randrange(1,1000000000000,2))
        for j in my_randoms:
            cola.enqueue(j)
        start = time.clock()
        for j in range(len(my_randoms)):
            cola.dequeue()
        end = time.clock()
        timing.append(end-start)
        my_randoms.clear()
    sum_timing=0
    for i in timing:
        sum_timing+=i
    average=sum_timing/200
    print("The average time is {}".format(average))
    sorted(timing)
    median=(timing[99]+timing[100])/2
    print("The median is {}".format(median))
    varience=0
    for i in timing:
        varience+=(i-average)**2
    print("The varience is {}".format(varience/199))
