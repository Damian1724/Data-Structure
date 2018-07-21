/*
Author: Damian Cruz
*/


import random
my_tree=BinarySearchTree()
my_randoms=[]
#in the first loop i am generating 10000 random numbers and inserting them into "my_randoms". 
#From 1 to 10000000 with step of 3
for i in range(10000):
    my_randoms.append(random.randrange(1,10000000,3))
#In the second loop i am adding the numbers to the tree 
for i in my_randoms:
    my_tree.insert(i)    
# Here i am checking if the number were placed correctly in the tree, the method "contain" should always return true 
#to any number in "my_randoms".
#For example i chose the 9977 position but any user who use  this code can change the position number.
output=my_tree.contain(my_randoms[9977])
