import os
# Doubly Linked list
class Node:
    def __init__(self,data): # doubly linked list takes data and 2 pointers (next and prev)
        self.data = data
        self.next = None
        self.prev = None

class dLL: # whole class is same as singly linked list by only difference is 
            # of 2 pointers (it enables us to traverse list in 2 direction)
    def __init__(self): 
        self.head = None

    def length(self):
        length = 0
        cur = self.head
        while cur != None: # if cur.next is used it will not count the last node
            cur = cur.next
            length+=1

        return length # returns num of node

    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def insertStart(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        self.head.next = temp
        temp.prev = self.head

    def insertAt(self,pos,data):
        node = Node(data)
        ind = 0
        cur = self.head
        while cur != None:
            if pos == 0:
                self.insertStart(data)
                break
            elif pos == self.length():
                self.append(data)
                break
            elif pos == ind:
                cur.prev.next = node
                node.next = cur
                cur.prev = node
                node.prev = cur.prev
                break
            elif pos > self.length():
                print "ERROR : list index out of range"
                break
            ind +=1
            cur = cur.next

    def pop(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.prev.next = None # this is the advantage of 2 pointers. (instead of using extra variable for storing previous data of lastnode, we used prev pointer to access )

    def deleteStart(self):
        self.head = self.head.next
        self.head.prev = None # making sure that prev data to head node is removed such that no extra space is assigned to it
 
    def deleteAt(self,pos):
        ind = 0
        cur = self.head
        while cur != None:
            if pos == 0:
                self.deleteStart()
                break
            
            elif pos == self.length():
                self.pop()
                break
            
            elif pos == ind:
                cur.prev.next = cur.next 
                cur.next.prev = cur.prev
                break
            
            elif pos > self.length():
                print "ERROR : list index out of range"
                break
            ind +=1
            cur = cur.next

    def display(self):
        cur = self.head
        while cur!=None:
            print cur.data
            cur = cur.next

    def reverse(self): # displays list in reverse order 
        cur = self.head
        while cur.next !=None : # to find last node
            cur = cur.next

        while cur != self.head:
            print cur.data
            cur = cur.prev

        print self.head.data

os.system('cls')
lt = dLL()
lt.append('A')
lt.append('B')
lt.append('C')
lt.insertStart('D')
lt.insertAt(4,'E')
lt.pop()
lt.deleteStart()
lt.deleteAt(1)
lt.display()
#print lt.length()
print "--Reverse--"
lt.reverse()