/*
Author:Damian Cruz
*/


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class MyQueue_LinkedList:

   def __init__(self):
       self.head=Node()
       self.tail=self.head
       self.size=0

   def is_empty(self):
       return self.size ==0

   def enqueue(self,element):
       self.size+=1
       self.tail.next=Node(element)
       self.tail=self.tail.next

   def dequeue(self):
       if self.size > 0:
           self.head.next=self.head.next.next
           self.size-=1
       else:
           raise Exception("The queue is empty")

   def lenght(self):
       return self.size



