/*
Author: Damian Cruz
*/



class Node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,element):
        if self.root is None:
            self.root=Node(element)
        else:
            self._insert(element,self.root)

    def _insert(self,element,current):
        if current.value > element:
            if current.left_child is None:
                current.left_child=Node(element)
            else:
                self._insert(element,current.left_child)
        if current.value < element:
            if current.right_child is None:
                current.right_child=Node(element)
            else:
                self._insert(element,current.right_child)

    def height(self):
        if self.root is None:
            return None
        else:
            return self._height(self.root,0)

    def _height(self, current,level):
        if current is None:
            return level
        return max(self._height(current.left_child,level+1),self._height(current.right_child,level+1))

    def contain(self,element):
        current=self.root
        while current.value != element:
            if current.value > element:
                if current.left_child is None:
                    return False
                else:
                    current=current.left_child
            if current.value < element:
                if current.right_child is None:
                    return False
                else:
                    current=current.right_child
        return True

    def lowest_common_ancestor(self, v1, v2):
        return self._lowest_common_ancestor(v1, v2, self.root)

    def _lowest_common_ancestor(self, v1, v2, current):
        if current.value > v1 and current.value > v2 and current.left_child is not None:
            self._lowest_common_ancestor(v1, v2,current.left_child)
        elif current.value < v1 and current.value < v2 and current.right_child is not None:
            self._lowest_common_ancestor( v1, v2,current.right_child)
        else:
            return current.value

    def preorder_traversal(self):
       return self._preorder_traversal(self.root,lista=[])

    def _preorder_traversal(self,current,lista):
        if current is not None:
            lista.append(current.value)
            self._preorder_traversal(current.left_child,lista)
            self._preorder_traversal(current.right_child,lista)
        return lista

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, lista=[])

    def _postorder_traversal(self,current,lista):
        if current is not None:
            self._postorder_traversal(current.left_child,lista)
            self._postorder_traversal(current.right_child,lista)
            lista.append(current.value)
        return lista

    def in_order(self):
        return self._in_order(self.root,lista=[])

    def _in_order(self,current,lista):
        if current is not None:
            self._in_order(current.left_child,lista)
            lista.append(current.value)
            self._in_order(current.right_child,lista)
        return lista
