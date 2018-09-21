import os
# Singly Linked List
class Node: # Node class takes data and next (pointer) allocation memory
    def __init__(self,data):
        self.data = data  
        self.next = None

class sLL:
    def __init__(self): # will initialize the head (start) node and points to next node as per list
        self.head = None

    def length(self):
        length = 0
        cur = self.head 
        while cur != None: # if cur.next is used it will not count the last node
            cur = cur.next
            length+=1

        return length # returns num of node

    def append(self,data): # adds node at the end of every previous node
        node = Node(data)

        if self.head == None:
            self.head = node

        else:
            cur = self.head # a temporary var(cur) is used such that when we loop our head node doesn't lose its value
            while cur.next != None:
                cur = cur.next

            cur.next = node

    def insertStart(self,data): # add node at the start
        node = Node(data) # node will have data and next  allocation memory

        temp = self.head
        self.head = node
        self.head.next = temp

    def insertAt(self,pos,data):
        node = Node(data)
        ind = 0
        cur = self.head
        while cur != None: # will terminate if next of last node will be None
            if pos == 0:
                self.insertStart(data)
                break
            elif pos == self.length():
                self.append(data)
                break
            elif pos == ind:
                prev.next = node
                node.next = cur
                break
            elif pos > self.length():
                print "ERROR : list index out of range"
                break
            ind+=1
            prev = cur
            cur = cur.next


    def pop(self):
        cur = self.head
        while cur.next != None: # returns last node (cur)
            prev = cur
            cur = cur.next
        
        #cur = None      # making last nodes data None will not change anything
        prev.next = None # thus previous of last node's reference should be done None                         

    def deleteStart(self):
        temp = self.head
        self.head = self.head.next
        temp = None # assigning None, we are making sure that it gets no memory. Otherwise it will still get a refernce which indirctly means it has some memory        

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
            elif pos > self.length():
                print "ERROR : list index out of range"
                break
            elif pos == ind:
                prev.next = cur.next
                break

            ind +=1
            prev = cur
            cur = cur.next

    def display(self):
        cur = self.head
        while cur != None:
            print cur.data
            cur = cur.next

os.system('cls')
lt = sLL()
lt.append(1)
lt.append(2)
lt.append(3)
lt.insertStart(4)
lt.insertStart(5)
lt.deleteStart()
lt.pop()
lt.insertAt(2,"A")
lt.deleteAt(5) 
#print lt.length()
lt.display()