class Node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None



class BinarySearchTree:
    def __init__(self):
        self.root=None



    def insert(self,element):
        _node_=Node(element)
        if self.root is None:
            self.root=_node_
        else:
            self._insert(element,self.root)


    def _insert(self,element,current):
        if current.value > element:
            if current.left_child is None:
                _node_=Node(element)
                current.left_child=_node_
            else:
                self._insert(element,current.left_child)
        if current.value < element:
            if current.right_child is None:
                _node_=Node(element)
                current.right_child=_node_
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
        return self._contain(self.root,element)


    def _contain(self,current,element):
        if current.value > element:
            if current.left_child is None:
                return False
            else:
                self._contain(current.left_child,element)
        elif current.value < element:
            if current.right_child is None:
                return  False
            else:
                self._contain(current.right_child,element)
        else:
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



    def Preorder_Traversal(self):
       return self._Preorder_Traversal(self.root,lista=[])


    def _Preorder_Traversal(self,current,lista):
        if current is not None:
            lista.append(current.value)
            self._Preorder_Traversal(current.left_child,lista)
            self._Preorder_Traversal(current.right_child,lista)
        return lista




    def Postorder_Traversal(self):
        return self._Postorder_Traversal(self.root, lista=[])

    def _Postorder_Traversal(self,current,lista):
        if current is not None:
            self._Preorder_Traversal(current.left_child,lista)
            self._Preorder_Traversal(current.right_child,lista)
            lista.append(current.value)
        return lista




    def In_Order(self):
        return self._In_Order(self.root,lista=[])


    def _In_Order(self,current,lista):
        if current is not None:
            self._In_Order(current.left_child,lista)
            lista.append(current.value)
            self._In_Order(current.right_child,lista)
        return lista
