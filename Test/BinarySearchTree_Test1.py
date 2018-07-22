/*
Author: Damian Cruz
*/


import random
my_tree=BinarySearchTree()
my_randoms=[]
for i in range(10000):
    my_randoms.append(random.randrange(1,1000000000000,3))
for i in my_randoms:
    my_tree.insert(i)

if len(my_tree.preorder_traversal()) > len(my_randoms):
    raise Exception("You are inserting numbers to the tree that do not belong to my_randoms")
else:
    print("The code is working perfectly")
