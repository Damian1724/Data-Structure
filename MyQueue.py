/*
Author:Damian Cruz
*/


class MyQueue:

    def __init__(self):
        self.lista = []
        self.size=0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        self.size += 1
        self.lista.append(element)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            self.lista.pop(0)
        else:
            raise Exception("The queue is empty")

    def lenght(self):
        return self.size
