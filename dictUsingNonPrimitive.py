import os
class ValueNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = ValueNode(value)
        self.next = None
        self.prev = None

class LL:
    def __init__(self):
        self.head = None

    def append(self,key,value):
        node = Node(key,value)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def delete(self):
        if self.head == None:
            print "Dictionary Empty!!. Nothing to Delete. First 'add' some words."
        else:
            opt = input("Select:\n1.Delete Key\n2.Delete Value\n:")
            found = False
            cur = self.head
            if opt == 1:
                k = raw_input("Provide Key to delete : ")
                while cur!=None:
                    if cur.key == k:
                        found = True
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                        cur = None
                    if cur == None:
                        break
                    cur = cur.next
                if found == False:
                    print "'"+k+"'","Not found. Try again."
            
            elif opt ==2:
                pass #------------R E M A N I N G--------------#
            
            else:
                c= input("%1.Delete OR 2.Quit%\n:")
                if c==1:
                    self.delete()
                else:
                    exit

    def update(self):
        if self.head == None:
            print "Dictionary Empty!!. First 'add' some words."
        else:
            opt = input("Select:\n1.Update Key\n2.Update Value\n:")
            found = False
            cur = self.head
            if opt == 1:
                k = raw_input("Enter Old Word : ")
                while cur != None:
                    if cur.key == k:
                        found = True
                        print "Enter New Word for '{}'".format(k)
                        n_k = raw_input(":")
                        cur.key = n_k # cur.key has data while cur only has reference to the data
                    if cur == None:
                        break
                    cur = cur.next
                if found == False:
                    print "'"+k+"'","Not found. Try again."
           
            elif opt ==2:
                pass #------------R E M A N I N G--------------#

            else:
                c = input("%1.Update OR 2.Quit%\n:")
                if c == 1:
                    self.update()
                else:
                    exit

    def search(self):
        if self.head == None:
            print "Dictionary Empty!!."
        else:
            opt = input("Select:\n1.Search Key\n2.Search Value\n:")
            found = False
            cur = self.head
            if opt == 1:
                k = raw_input("Enter Word to Search: ")
                while cur != None:
                    if cur.key == k:
                        found = True
                        print "Word and meaning is-\n",cur.key,":",cur.value.data
                    if cur == None:
                        break
                    cur = cur.next
                if found == False:
                    print "'"+k+"'","Not found. Try again."
           
            elif opt ==2:
                word_val = raw_input("Enter Word meaning to Search: ")
                while cur!=None:
                    if word_val in cur.value.data: # 'in' is used to find string from a string data type or/and list data type
                        found = True
                        print "Word and meaning is-\n-->",cur.key,":",cur.value.data
                    if cur==None:
                        break
                    cur = cur.next
                if found == False:
                    print "'"+word_val+"'","Not found. Try again."

            else:
                c = input("%1.Search OR 2.Quit%\n:")
                if c == 1:
                    self.search()
                else:
                    exit

    def display(self):
        os.system('cls')
        ind = 1
        cur = self.head
        print "*"*5,"D I C T I O N A R Y","*"*5
        if self.head == None:
            print "Dictionary Empty!!"
        while cur!=None:
            print ind,")",cur.key,":",cur.value.data
            cur = cur.next
            ind +=1
        print "*"*31
        
    def reverse(self):
        cur = self.head
        while cur.next !=None:
            cur = cur.next

        while cur!=self.head:
            print cur.key,":",cur.value.data
            cur = cur.prev
        print cur.key,":",cur.value.data

# dictionary object
dt = LL()
os.system('cls')
while True:
    print "-"*7,"Main Menu","-"*7
    print "Select From:\n1.Add\n2.Display\n3.Update\n4.Search\n5.Delete\n6.EXIT"
    print "-"*25
    opt = input("->")
    if opt == 1:
        key = raw_input("Enter Word : ")
        value = raw_input("Enter value (comma seperated): ")
        dt.append(key,value)
    elif opt == 2:
        dt.display()
        # print "--REVERSE--"
        # dt.reverse()
    elif opt == 3:
        dt.update()
    elif opt == 4:
        dt.search()
    elif opt == 5:
        dt.delete()
    elif opt == 6:
        os.system('cls')
        print "Program Terminated"
        break
    else:
        os.system('cls')
        print "Wrong selection. Try Again."