/*
Author: Damian Cruz
*/

#checking if all the numbers were placed correctly
import random
my_tree=BinarySearchTree()
my_randoms=[]
for i in range(10000):
    my_randoms.append(random.randrange(1,10000000,3))
for i in my_randoms:
    my_tree.insert(i)    
for i in my_randoms:
    if my_tree.contain(i) is False:
        raise Exception ("The number {} is not in the tree or it was misplaced it".format(i))
print("YES! ,the code is working")
