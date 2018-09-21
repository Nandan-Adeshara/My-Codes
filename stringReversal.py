# Reverse a Word of a String (Eg. NANDAN -> N A D N A N)
import os
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def display(self):
        cur = self.head
        while cur!= None:
            print cur.data
            cur = cur.next

while True:
    reverse = LL()
    c = input("Select:\n1.String Reversal\n2.Exit\n->")
    if c == 1:
        os.system('cls')
        word = list(raw_input("Enter Word : "))
        while True:
            if len(word) == 0:
                break
            reverse.push(word.pop())
        reverse.display()
    else:
        os.system('cls')
        break