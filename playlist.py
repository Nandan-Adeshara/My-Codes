import os
class Node:
    def __init__(self,song):
        self.song = song
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.cur  = None    

    def add(self,song):
        node = Node(song)

        if self.head == None:
            self.head = node

        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def play(self,song):
        os.system('cls')
        if self.head == None:
            print "Playlist is Empty."
        else:
            self.cur = self.head
            found = False
            while self.cur !=None:
                if self.cur.song == song: # cur.song is used as cur will give only refernce to the cur song's data
                    found = True
                    print "Now Playing - '{}'".format(self.cur.song)
                    return # return is used to end the loop such that current memory of self.cur is saved(as well as self.cur doesn't become None)
                self.cur = self.cur.next
            if found == False:
                print "Song '{}' not in the playlist.".format(song)

    def prev_next(self,c):
        os.system('cls')
        if self.cur == None:
            song = raw_input("No song playing. Select a song : ")
            self.play(song)
        elif c == 1:
            if self.cur.next == None:
                print "Current Song is the last song in Playlist."
            else:
                self.cur = self.cur.next # every time it comes it updates it self
                print "Playing next song -",self.cur.song
        elif c == 2:
            if self.cur.prev == None:
                print "Current Song is the First Song in Playlist."
            else:
                self.cur = self.cur.prev
                print "Playing previous song -",self.cur.song

    def show(self):
        os.system('cls')
        if self.head == None:
            print "Playlist is Empty."
        else:
            ind = 1
            print "Showing Playlist --"
            cur = self.head
            while cur != None:
                print "{}.".format(ind),cur.song 
                cur = cur.next
                ind +=1

            # print "--REVERSE--"
            # temp = self.head
            # while temp.next != None:
            #     temp = temp.next

            # while temp != self.head:
            #     print temp.song
            #     temp = temp.prev

            # print temp.song

song = Playlist()
os.system('cls')
while True:
    print "-"*15,"\nSelect:\n1.Add Song\n2.Display\n3.Play Song\n4.Play Next Song\n5.Play Prev Song\n6.EXIT\n","-"*15
    opt = input("->")
    if opt == 1:
        data = raw_input("Enter Song name into playlist : ")
        song.add(data)
        os.system('cls')
        print "'{}' Song added!!".format(data)
    elif opt ==2:
        song.show()
    elif opt ==3:
        data = raw_input("Which song do you want to play : ")
        song.play(data)
    elif opt == 4:
        song.prev_next(1)
    elif opt == 5:
        song.prev_next(2)
    else:
        os.system('cls')
        print "Music stoped."
        break