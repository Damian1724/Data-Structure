/*
Author:Damian Cruz
*/


class myqueue:
   def __init__(self):
       self.item=[]

   def is_empty(self):
       return self.item == []

   def enqueue(self,element):
       self.item.append(element)

   def dequeue(self):
       self.item.pop(0)

   def lenght(self):
       return len(self.item)
