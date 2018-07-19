/*
Author:Damian Cruz
*/


class myqueue:

    def __init__(self):
        self.lista = []
        self.size=0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        self.size += 1
        self.lista.append(element)

    def dequeue(self):
        self.size -= 1
        self.lista.pop(0)

    def lenght(self):
        return self.size

    
