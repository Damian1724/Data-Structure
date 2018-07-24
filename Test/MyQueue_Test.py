/*
Author:Damian Cruz
*/

#operations

def statistical_calculation(timing):
    sum_timing = 0
    for i in timing:
        sum_timing += i
        
    average = sum_timing / 200
    print("The average time is {}".format(average))
    sorted(timing)
    median = (timing[99] + timing[100]) / 2
    print("The median is {}".format(median))
    varience = 0
    for i in timing:
        varience += (i - average) ** 2
        
    print("The varience is {}".format(varience / 199))
    
def enqueue_timing(cola,my_randoms,timing):
    import time
    import random
    for j in range(10000):
        my_randoms.append(random.randrange(1, 1000000000000, 2))
        
    start = time.clock()
    for j in my_randoms:
        cola.enqueue(j)
        
    end = time.clock()
    timing.append(end - start)
    my_randoms.clear()
   

def dequeue_timing(cola,my_randoms,timing):
    import time
    import random
    for j in range(10000):
        my_randoms.append(random.randrange(1, 1000000000000, 2))
        
    for j in my_randoms:
        cola.enqueue(j)
        
    start = time.clock()
    for j in range(len(my_randoms)):
        cola.dequeue()
        
    end = time.clock()
    timing.append(end - start)
    my_randoms.clear()
    

# These two methods are for MyQueue

def enqueue():
    my_randoms = []
    timing = []
    cola=MyQueue()
    for i in range(200):
        enqueue_timing(cola,my_randoms,timing)
        
    statistical_calculation(timing)
    
def dequeue():
    my_randoms = []
    timing = []
    cola = MyQueue()
    for i in range(200):
        dequeue_timing(cola,my_randoms,timing)
        
    statistical_calculation(timing)

#These two methods are for Myqueue_LinkedList    
    
def enqueue():
    my_randoms = []
    timing = []
    for i in range(200):
        cola=MyQueue_LinkedList()
        enqueue_timing(cola,my_randoms,timing)
        
    statistical_calculation(timing)
    
 def dequeue():
    my_randoms = []
    timing = []
    for i in range(200):
        cola=MyQueue_LinkedList()
        dequeue_timing(cola,my_randoms,timing)
        
    statistical_calculation(timing)
