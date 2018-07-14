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


   def is_empty(self):
       if self.size ==0:
           return True
       return False


   def enqueue(self,element):
       self.size+=1
       _node_=Node(element)
       current=self.head
       while current.next is not None:
           current=current.next
       current.next=_node_


   def dequeue(self):
       self.head.next=self.head.next.next
       self.size-=1


   def lenght(self):
       return self.size
