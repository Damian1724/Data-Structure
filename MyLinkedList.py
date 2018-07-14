/*
Author:Damian Cruz
*/

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class MyLinkedList:
    def __init__(self):
        self.head=Node()


    def append(self,data):
        currrent=self.head
        new_node=Node(data)
        while currrent.next is not None:
            currrent=currrent.next
        currrent.next=new_node


    def lenght(self):
        current=self.head
        total=0
        while current.next is not None:
            total+=1
            current=current.next
        return total


    def display(self):
        current=self.head.next
        while current.next is not None:
            print(current.data,end=" ")
            current=current.next
        print(current.data)


    def get(self,index):
        if index > self.lenght():
            print("ERROR: Index out of range")
            return None
        current=self.head
        pos=0
        while True:
            current = current.next
            if pos==index:
                return current.data
            pos+=1


    def erase(self,index):
        if index > self.lenght():
            print("ERROR: Index out of range")
            return
        current_node=self.head
        pos=0
        while True:
            last_node=current_node
            current_node=current_node.next
            if pos==index:
                last_node.next=current_node.next
                return
            pos+=1
