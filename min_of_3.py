# to create a class which shows minimum from 3 no. given by the user

class Number:
    ''' minimum from a given 3 int or float no.'''
    def __init__(self):
        self.a='a'
        self.b='b'
        self.c='c'
        
    def input(self):
        self.a=input("Enter 1st number: \n")
        self.b=input("Enter 2nd number: \n")
        self.c=input("Enter 3rd number: \n")
    
    def minimum(self):
        if self.a<self.b and self.a<self.c:
            print self.a
        elif self.b<self.a and self.b<self.c:
            print self.b
        else:
            print self.c
          
while True:
    mini_no=Number()
    mini_no.input() 
    mini_no.minimum()
