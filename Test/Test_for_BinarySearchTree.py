/*
Author: Damian Cruz
*/


import random
my_tree=BinarySearchTree()
my_randoms=[]
for i in range(10000):
    my_randoms.append(random.randrange(1,10000000,3))
for i in my_randoms:
    my_tree.insert(i)    
for i in my_randoms:
    if my_tree.contain(i) is False:
        raise Exception ("The number",i, "is not in the tree or it was misplaced it")
print("YES! ,the code is working")
