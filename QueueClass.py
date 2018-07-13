/*
Author:Damian Cruz
*/


class myqueue:
   def __init__(self):
       self.item=[]

   def print_number(self,position):
       print(self.item[position])

   def add_number(self,number):
       self.item.append(number)

   def print_queue(self):
       print(self.item[:])

   def remove_first_elemt(self):
       self.item.pop(0)

   def lenght_of_queue(self):
       print(len(self.item))
