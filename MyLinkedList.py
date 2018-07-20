/*
Author:Damian Cruz
*/



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size=0

    def enqueue(self, data):
        self.size += 1
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def lenght(self):
        return self.size

    def get(self, index):
        if index > self.size or index < 0:
            raise Exception("ERROR: Index out of range")
        current = self.head
        pos = 0
        while pos <= index:
            pos += 1
            current = current.next
        return current.data

    def dequeue(self, index):
        if index > self.size or index < 0:
            raise Exception("ERROR: Index out of range")
        self.size -= 1
        current= self.head
        pos = 0
        while pos <= index:
            last_node = current
            current = current.next
            pos += 1
        last_node.next = current.next

    def reverse(self):
        if self.size >= 2:
            output = Node(self.head.data)
            while self.head.next is not None:
                self.head = self.head.next
                aux = output
                add_node = Node(self.head.data)
                output = add_node
                output.next = aux
            self.head = output
        elif self.size == 0:
            raise Exception("The LinkedList is empty")
        else:
            raise Exception("The LinkedList has just one element")

    def get_linked_list(self):
        if self.size > 0:
            current = self.head.next
            lista = []
            while current.next is not None:
                lista.append(current.data)
                current = current.next
            lista.append(current.data)
            return lista
        else:
            raise Exception("The LinkedList is empty")
