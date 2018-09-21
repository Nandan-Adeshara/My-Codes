# Inorder Traversal
# Rules- if element is less than the current node than it goes in the left subtree,
#        else it will be greater than equal to the current node and goes in right subtree.

import os
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        self.right = None
        self.left  = None

class Traversal:
    def __init__(self):
        self.root = None # root of the tree
        self.temp = None # temp is used to store the detail for temporary purpose (like for reversal of string)

    def append(self,data):
        node = Node(data)

        if self.root == None:
            self.root = node
        else:
            cur = self.root
            while cur.next !=None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def display(self):
        os.system('cls')
        if self.root == None:
            print "No data"
        else:
            self.temp = self.root
            while self.temp.next!=None:
                print self.temp.data
                self.temp = self.temp.next
            print self.temp.data # to print the last node

    def reverse(self):
        if self.temp == None:
            print " No data "
        else:
            while self.temp != self.root:
                print self.temp.data
                self.temp = self.temp.prev
            print self.temp.data # to print the root node

lt = Traversal()
while True:
    opt = input("1. Add\n2. Exit\n:")
    if opt == 1:
        data = raw_input("Enter some data : ")
        lt.append(data)
        c = raw_input("Print the message (Y/N) ? :").lower()
        if c == "y":
            lt.display()
        else:
            pass
    elif opt == 2:
        break