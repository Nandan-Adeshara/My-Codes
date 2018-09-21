import os
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class cLL: # circular linked list's first and last pointer points each other (main difference)
    def __init__(self):
        self.head = None

    def length(self):
        length = 0
        cur = self.head
        while True:
            cur = cur.next
            length+=1
            if cur == self.head: # we are stopping loop at head such that it will be counted( when we started it did not counted head as it directily assigned from next of head node)
                break

        return length

    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head

        else:
            cur = self.head
            while True: # during circular linked list we can check the condition by checking if the node is visited
                cur = cur.next
                if cur.next== self.head: # to check last node, last node's next should be head
                    break

            cur.next = node 
            node.next = self.head # as new node's next will always be pointing to head 
            node.prev = cur # new node's previous will point to the last node
            self.head.prev = node # we knew that node's next will be head, such that is was pretty sure that head's previous will be new node

    def insertStart(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        temp.prev.next = self.head
        self.head.next = temp
        self.head.prev = temp.prev
        temp.prev = self.head

    def insertAt(self,pos,data):
        node = Node(data)
        ind = 0
        cur = self.head
        while True:
            if pos == 0:
                self.insertStart(data)
                break
            if pos == self.length():
                self.append(data)
                break
            if pos == ind:
                cur.prev.next = node
                node.next = cur
                node.prev = cur.prev
                cur.prev = node
                break
            if pos>self.length():
                print "ERROR : list index out of range"
                break
            cur = cur.next
            ind +=1

    def pop(self):
        cur = self.head
        while True:
            cur = cur.next
            if cur.next == self.head:
                break

        self.head.prev = cur.prev #only next of last's previous and head's next needs to refernce. Rest nodes have sufficiet reference
        cur.prev.next = self.head
        cur = None # memory and data is destroyed if set to None

    def deleteStart(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = temp.prev
        temp.prev.next = self.head
        temp = None
        
    def deleteAt(self,pos):
        ind = 0
        cur = self.head
        while True:
            if pos == 0:
                self.deleteStart()
                break
            if pos == self.length():
                self.pop()
                break
            if pos == ind:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                break
            if pos>self.length():
                print "ERROR : list index out of range"
                break
            cur = cur.next
            ind +=1

    def display(self):
        cur = self.head
        while True:
            print cur.data
            cur = cur.next
            if cur == self.head: # it will stop the loop if the node is visited and printed
                break

    def reverse(self):
        cur = self.head
        while True:
            print cur.prev.data
            cur = cur.prev
            if cur == self.head:
                break
os.system('cls')
lt = cLL()
lt.append(3)
lt.append(2)
lt.append(1)
lt.append("B")
lt.insertStart("C")
lt.insertAt(2,"A")
lt.pop()
lt.pop()
lt.deleteStart()
lt.deleteAt(1)
lt.display()
print "--Reverse--"
lt.reverse()