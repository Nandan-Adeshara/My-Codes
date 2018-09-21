import os

class DM:
    ''' Class for storing the list of units and values and converting items
        into necessary unit value'''
    avl_units = ['m','km','cm']    
        
    def __init__(self,*args):
        self.unit  = None
        self.value = None
        self.var   = args
        self.conv  = None
        self.count = []
        
    
       
    def input(self):
        
        self.unit  = raw_input("Enter Unit  : ")
            
        while True:
            if self.unit == 'm' or self.unit == 'cm' or self.unit == 'km':
                print "Unit Accepted"
                break
            else:    
                print "Unit Not Accepted"
                print "Available units are-[m,cm,km]"
                self.unit = raw_input("Enter unit from above selection: ")       
        self.value = input("Enter value : ")
        self.var   = str(self.value) + self.unit
        

    def __add__(self,other):
        if other.unit != 'm':   
            if other.unit == 'km':
                other.conv = 1000*other.value
                print "Converted value of {} is {}m".format(other.var,other.conv)
                add = self.value + other.conv
                print "Addition of- \n   {} + {} = {}{}".format(self.var,other.var,add,self.unit)
                
            elif other.unit == 'cm':
                other.conv = other.value/100
                print "Converted value of {} is {}m".format(other.var,other.conv)
                add = self.value + other.conv
                print "Addition of- \n   {} + {} = {}{}".format(self.var,other.var,add,self.unit)
        
        elif other.unit !='cm':
            if other.unit == 'km':
                other.conv = 100000*other.value
                print "Converted value of {} is {}cm".format(other.var,other.conv)
                add = self.value + other.conv
                print "Addition of- \n   {} + {} = {}{}".format(self.var,other.var,add,self.unit)
            
            elif other.unit == 'm':    
                other.conv = other.value*100
                print "Converted value of {} is {}cm".format(other.var,other.conv)
                add = self.value + other.conv
                print "Addition of- \n   {} + {} = {}{}".format(self.var,other.var,add,self.unit)
                
        elif other.unit !='km':    
            if other.unit == 'cm':
                other.conv = other.value/100000
                print "Converted value of {} is {}km".format(other.var,other.conv)
                add = self.value + other.conv
                print "Addition of- \n   {} + {} = {}{}".format(self.var,other.var,add,self.unit)
            elif other.unit == 'm':
                other.conv = other.value/1000
                print "Converted value of {} is {}km".format(other.var,other.conv)
                add = self.value + other.conv
                print "Addition of- \n   {} + {} = {}{}".format(self.var,other.var,add,self.unit)    
                
        
    def __sub__(self,other):
        if other.unit != 'm':
            if other.unit == 'km':
                other.conv = 1000*other.value
                print "Converted value of {} is {}m".format(other.var,other.conv)
                if self.value > other.conv:
                    sub = self.value - other.conv
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                else:
                    sub = other.conv - self.value
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                
            elif other.unit == 'cm':
                other.conv = other.value/100
                print "Converted value of {} is {}m".format(other.var,other.conv)
                if self.value > other.conv:
                    sub = self.value - other.conv
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                else:
                    sub = other.conv - self.value
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                    
                    
        
        elif other.unit !='cm':
            if other.unit == 'km':
                other.conv = 100000*other.value
                print "Converted value of {} is {}cm".format(other.var,other.conv)
                if self.value > other.conv:
                    sub = self.value - other.conv
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                else:
                    sub = other.conv - self.value
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
            
            elif other.unit == 'm':    
                other.conv = other.value*100
                print "Converted value of {} is {}cm".format(other.var,other.conv)
                if self.value > other.conv:
                    sub = self.value - other.conv
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                else:
                    sub = other.conv - self.value
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                
        elif other.unit !='km':    
            if other.unit == 'cm':
                other.conv = other.value/100000
                print "Converted value of {} is {}km".format(other.var,other.conv)
                if self.value > other.conv:
                    sub = self.value - other.conv
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                else:
                    sub = other.conv - self.value
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
            elif other.unit == 'm':
                other.conv = other.value/1000
                print "Converted value of {} is {}km".format(other.var,other.conv)
                if self.value > other.conv:
                    sub = self.value - other.conv
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit)
                else:
                    sub = other.conv - self.value
                    print "Subtraction of- \n   |{} - {}| = {}{}".format(self.var,other.var,sub,self.unit) 
            
    def __gt__(self,other):
        if self.unit == 'm':
            if other.unit == 'km':
                other.conv = 1000*other.value
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            elif other.unit == 'cm':    
                other.conv = other.value/100
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            else:
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
        
        elif self.unit == 'cm':
            if other.unit == 'km':
                other.conv = 10000*other.value
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            elif other.unit == 'm':
                other.conv = 100*other.value
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            else:
                if self.value > other.value:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
                    
        elif self.unit == 'km':
            if other.unit == 'm':
                other.conv = other.value/1000
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            elif other.unit == 'cm':
                other.conv = other.value/100000
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            else:
                if self.value > other.conv:
                    print "True: {} is Greater than {}".format(self.var,other.var)
                else:
                    print "False: {} is not Greater than {}".format(self.var,other.var)
            

os.system('cls')            
a1 = DM()
a1.input()

a2 = DM()
a2.input()

a3 = DM()
a3.input()

a1 + a2
a1 - a2
a2 > a1