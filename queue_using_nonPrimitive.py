class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        #self.left  = None

class Queue:
    def __init__(self):
        self.rear  = None
        self.front = None

    def enqueue(self,data):
        node = Node(data)

        if self.rear == None:
            self.rear = node
            self.front = self.rear
        else:
            cur = self.rear
            while cur.right != None:
                cur = cur.right

            cur.right = node

    def dequeue(self):
        if self.front is None:
            print "List Empty."
        else:
            temp = self.front
            self.front = self.front.right
            temp = None

    def display(self):
        cur = self.front
        while cur != None:
            print cur.data
            cur = cur.right

queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(2)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()