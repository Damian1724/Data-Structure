class Node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class MyTree:
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
        if current.value == element:
            raise Exception("the element is already in the tree")

    def is_a_bst(self):
        aux=0
        value=self._is_a_bst(self.root,aux)
        if value is None:
            return True
        else:
            return False

    def _is_a_bst(self,current,aux):
        if current is not None:
            self._is_a_bst(current.left_child,aux)
            if aux < current.value:
                aux=current.value
            else:
                return False
            self._is_a_bst(current.right_child,aux)


    def height(self):
        if self.root is None:
            return None
        else:
            return self._height(self.root,0)



    def _height(self,current,level):
        if current is None:
            return level

        return max(self._height(current.left_child,level+1),self._height(current.right_child,level+1))
