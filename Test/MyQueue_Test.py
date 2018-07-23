/*
Author:Damian Cruz
*/
def MyQueue_timing():
    import time
    import random
    my_randoms=[]
    cola=MyQueue()
    timing_enqueue=[]
    timing_dequeue=[]
    for i in range(200):
        for j in range(10000):
            my_randoms.append(random.randrange(1,1000000000000,2))
        start=time.clock()
        for j in my_randoms:
            cola.enqueue(j)
        end = time.clock()
        timing_enqueue.append(end-start)
        start = time.clock()
        for j in range(len(my_randoms)):
            cola.dequeue()
        end = time.clock()
        timing_dequeue.append(end-start)
        my_randoms.clear()
    sum_enqueue=0
    sum_dequeue=0
    for i in range(200):
        sum_enqueue+=timing_enqueue[i]
        sum_dequeue+=timing_dequeue[i]
    average_enqueue=sum_enqueue/200
    average_dequeue=sum_dequeue/200
    print("The average time for enqueue is {} and for dequeue is {}".format(average_enqueue,average_dequeue))
    sorted(timing_enqueue)
    sorted(timing_dequeue)
    median_enqueue=(timing_enqueue[99]+timing_enqueue[100])/2
    median_dequeue=(timing_dequeue[99]+timing_dequeue[100])/2
    print("The median for enqueue is {} and for dequeue is {}".format(median_enqueue,median_dequeue))
    varience_enqueue=0
    variance_dequeue=0
    for i in range(200):
        varience_enqueue+=(timing_enqueue[i]-average_enqueue)**2
        variance_dequeue+=(timing_dequeue[i]-average_dequeue)**2
    print("The varience for enqueue is {} and for dequeue is {}".format(varience_enqueue/199,variance_dequeue/199))
    print(varience_enqueue/199)
