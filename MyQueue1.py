/*
Author:Damian Cruz
*/


class myqueue:

   size=0

   def __init__(self):
       self.lista=[]
   


   def is_empty(self):
       if self.size ==0:
           return True
       return False


   def enqueue(self,element):
       self.size+=1
       self.lista.append(element)


   def dequeue(self):
       self.size-=1
       self.lista.pop(0)


   def lenght(self):
       return self.size

   def print(self):
       print(self.lista)
