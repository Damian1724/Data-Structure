/*
Author: Damian Cruz
*/

#checking if all the numbers were placed correctly
def inserting():
    import random
    my_tree=BinarySearchTree()
    my_randoms=[]
    for i in range(10000):
        my_randoms.append(random.randrange(1,1000000000000,3))
    my_randoms.append(0)
    for i in my_randoms:
        my_tree.insert(i)
    if len(my_tree.preorder_traversal()) > len(my_randoms):
        raise Exception("You are inserting numbers to the tree that do not belong to my_randoms")
    print("The code is working perfectly")

#cheking if numbers outside of my_randoms were added
def checking():
    import random
    my_tree = BinarySearchTree()
    my_randoms = []
    for i in range(10000):
        my_randoms.append(random.randrange(1, 10000000, 3))
    for i in my_randoms:
        my_tree.insert(i)
    for i in my_randoms:
        if my_tree.contain(i) is False:
            raise Exception("The number {} is not in the tree or it was misplaced it".format(i))
    print("YES! ,the code is working")
