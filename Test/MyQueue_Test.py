/*
Author:Damian Cruz
*/

#operations

def statistical_calculation(timing,n):
    sum_timing = 0
    for i in timing:
        sum_timing += i

    average = sum_timing / n
    sorted(timing)
    median = (timing[int((n/2)-1)] + timing[int(n/2)]) / 2
    varience = 0
    for i in timing:
        varience += (i - average) ** 2

    return average,median,varience

def enqueue_timing(cola):
    import time
    import random
    my_randoms = []
    for j in range(10000):
        my_randoms.append(random.randrange(1, 1000000000000, 2))

    start = time.clock()
    for j in my_randoms:
        cola.enqueue(j)

    end = time.clock()
    return end - start

def dequeue_timing(cola):
    import time
    import random
    my_randoms = []
    for j in range(10000):
        my_randoms.append(random.randrange(1, 1000000000000, 2))

    for j in my_randoms:
        cola.enqueue(j)

    start = time.clock()
    for j in range(len(my_randoms)):
        cola.dequeue()

    end = time.clock()
    return end - start

# These two methods are for MyQueue

def enqueue():
    timing = []
    n=200
    cola=MyQueue()
    for i in range(n):
        timing.append(enqueue_timing(cola))

    average,median,varience=statistical_calculation(timing,n)
    print(average,median,varience)

def dequeue():
    timing = []
    n=200
    cola=MyQueue()
    for i in range(n):
        timing.append(dequeue_timing(cola))
        
    average,median,varience=statistical_calculation(timing,n)
    print(average,median,varience)
    
#These two methods are for Myqueue_LinkedList    

def enqueue():
    timing = []
    n=200
    for i in range(n):
        cola=MyQueue_LinkedList()
        timing.append(enqueue_timing(cola))

    average,median,varience=statistical_calculation(timing,n)
    print(average,median,varience)

def dequeue():
    timing = []
    n=200
    for i in range(n):
        cola=MyQueue_LinkedList()
        timing.append(dequeue_timing(cola))
        
    average,median,varience=statistical_calculation(timing,n)
    print(average,median,varience)
