/*
Author:Damian Cruz
*/


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class myqueue:

   size=0

   def __init__(self):
       self.head=Node()
       self.aux=self.head


   def is_empty(self):
       if self.size ==0:
           return True
       return False


   def enqueue(self,element):
       self.size+=1
       _node_=Node(element)
       self.aux.next=_node_
       self.aux=self.aux.next


   def dequeue(self):
       self.head.next=self.head.next.next
       self.size-=1


   def lenght(self):
       return self.size
