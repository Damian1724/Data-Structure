/*
Author:Damian Cruz
*/


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkedList:
    
    size = 0

    def __init__(self):
        self.head = Node()
        self.aux=self.head

 
    def append(self, data):
        self.size += 1
        new_node = Node(data)
        self.aux.next = new_node
        self.aux=self.aux.next


    def lenght(self):
        return self.size


    def get(self, index):
        if index > self.size:
            raise Exception("ERROR: Index out of range")
            return None
        current = self.head
        pos = 0
        while True:
            current = current.next
            if pos == index:
                return current.data
            pos += 1


    def remove(self, index):
        if index > self.size:
            raise Exception("ERROR: Index out of range")
            return
        self.size -= 1
        current_node = self.head
        pos = 0
        while True:
            last_node = current_node
            current_node = current_node.next
            if pos == index:
                last_node.next = current_node.next
                return
            pos += 1


    def reverse(self):
        if self.head == Node or self.head.next is None:
            return self.head
        output = Node(self.head.data)
        while self.head.next is not None:
            self.head = self.head.next
            aux = output
            add_node = Node(self.head.data)
            output = add_node
            output.next = aux
        self.head = output
        return add_node


    def get_linked_list(self):
        current=self.head
        lista=[]
        while current.next is not None:
            lista.append(current.data)
            current=current.next
        lista.append(current.data)
        return lista

