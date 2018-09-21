class Rational:
    ''' All the arithmetic operations are involved using
    operator overloading'''
    
    def __init__(self, a , b):
        
        self.a = a
        self.b = b
        
    @property
    def disp(self):
        
        self.x = "{}/{}" .format(self.a,self.b)
        print self.x
    
    #@property
    def __add__(self,other):
        #Rational.disp
        x = (self.a*other.b) + (self.b*other.a)
        y = self.b*other.b
        sum = str(x) + "/" + str(y)
        print "\n{} + {} = {}" .format(self.x,other.x,sum)
    
    def __sub__(self,other):
        x = (self.a*other.b) - (self.b*other.a)
        y = self.b*other.b
        sum = str(x) + "/" + str(y)
        print "\n{} + {} = {}" .format(self.x,other.x,sum)

    
    def __mul__(self,other):
        x = self.a*other.a
        y = self.b*other.b
        sum = str(x) + "/" + str(y)
        print "\n{} + {} = {}" .format(self.x,other.x,sum)
        
    
    def __div__(self,other):
        x = (self.a*other.b) + (self.b*other.a)
        y = self.b*other.b
        sum = str(x) + "/" + str(y)
        print "\n{} + {} = {}" .format(self.x,other.x,sum)
        
    def __ne__(self,other):
        if self.a != other.a or self.b != other.b:
            print "\n{} != {} is {}" .format(self.x,other.x,True)
        else:
            print "\n{} != {} is {}" .format(self.x,other.x,False)
        
    def __eq__(self,other):
        if self.a == other.a and self.b == other.b:
            print "\n{}={} is {}" .format(self.x,other.x,True)    
        else:    
            print "\n{}={} is {}" .format(self.x,other.x,False)
        
    def __lt__(self,other):
        if self.a < other.a and self.b < other.b:
            print "\n{} < {} is {}" .format(self.x,other.x,True)
        else:
            print "\n{} < {} is {}" .format(self.x,other.x,False)
        
    def __le__(self,other):
        if self.a <= other.a and self.b <=other.b:
            print "\n{} <= {} is {}" .format(self.x,other.x,True)
        else:
            print "\n{} <= {} is {}" .format(self.x,other.x,False)
        
    def __gt__(self,other):
        if self.a > other.a or self.b > other.b:
            print "\n{} > {} is {}" .format(self.x,other.x,True)
        else:
            print "\n{} > {} is {}" .format(self.x,other.x,False)
        
    def __ge__(self,other):
        if self.a >= other.a or self.b >=other.b:
            print "\n{} >= {} is {}" .format(self.x,other.x,True)
        else:
            print "\n{} >= {} is {}" .format(self.x,other.x,False)
        
r1 = Rational(5,2)
r2 = Rational(4,3)
r3 = Rational(6,4)

r1.disp
r2.disp
r3.disp
#Rational.__add__(r1,r2)  - can also be called like this
#r1.__sub__(r2)
#r1.__mul__(r2)
print "-"*5+"Main Part"+"-"*5
r1 + r2
r1 - r2
r1 * r2
r1 / r2
r1 !=r2
r1 ==r2
r1 > r2
r1 >=r2
r1 < r2
r1 <=r2
print "-"*20