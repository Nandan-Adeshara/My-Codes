import os
import time
from datetime import date

class Queue():
    # temporary list stores data. Data is only updated and Deleted from this list.
    # temporary list should be deleted at the end of day.
    # main list stores all the person records from day 1.
    today =date.today()

    def __init__(self):
        self.temp = []          #temporarily saves 
        self.main = []          #permanently saves

    def add(self,list):
        self.temp.append(list)
        self.main.append(list)

    def fileHandler(self,filename):
        sr = 1
        with open(filename,'w') as mainFile:
            mainFile.write("Customer Details: \n")
            for i in self.main:
                mainFile.write('\n')
                mainFile.write(str(sr)+ '.' +i.keys()[0] + '=' + str(i.values()[0]))
                sr+=1
                if i.keys()[0] == 'State':
                    sr=1
                    mainFile.write('\n')

    def display(self):
        #print self.temp[-1].values()[0]
        sr = 1
        cus = 1
        mainCounter = 0
        print "-"*30,"\nCustomer Details:- \nCustomer {}--\n".format(cus)
        for i in self.temp:
            print str(sr)+".",i.keys()[0]," = ",i.values()[0]
            sr+=1
            mainCounter+=1
            if i.keys()[0] == 'State':
                cus+=1
                sr = 1
                if len(self.temp)==mainCounter:
                    print "-"*30
                    break
                print '\nCustomer {}---'.format(cus)

    def delete(self,name_index):
        i=0
        while i<5:
            del self.temp[name_index]
            i+=1

    def search(self,date,month,year):
        if today.day == date:
            sr = 1
            cus = 1
            mainCounter = 0
            print "-"*30,"\nCustomer Details:- \nCustomer {}--\n".format(cus)
            for i in self.main:
                print str(sr)+".",i.keys()[0]," = ",i.values()[0]
                sr+=1
                mainCounter+=1
                if i.keys()[0] == 'State':
                    cus+=1
                    sr = 1
                    if len(self.main)==mainCounter:
                        print "-"*30
                        break
                    print '\nCustomer {}---'.format(cus)
            
    def mainList(self):
        sr = 1
        cus = 1
        mainCounter = 0
        print "-"*30,"\nCustomer Details:- \nCustomer {}--\n".format(cus)
        for i in self.main:
            print str(sr)+".",i.keys()[0]," = ",i.values()[0]
            sr+=1
            mainCounter+=1
            if i.keys()[0] == 'State':
                cus+=1
                sr = 1
                if len(self.main)==mainCounter:
                    print "-"*30
                    break
                print '\nCustomer {}---'.format(cus)

# Object Method
os.system('cls')
filename = 'Bank Details.txt'
lt = Queue()
today = date.today()    
while True:
    print "\n","*"*30,"\n1.ADD Customer \n2.DISPLAY Customer \n3.DELETE Customer \n4.SEARCH Customer \n5.PRINT Main List \n6.SAVE in FILE \n7.EXIT\n","*"*30
    ch = input("Enter choice : ")
    start = time.clock()
    if ch == 1:
        os.system('cls')
        # name, date , address , city , state
        k1,v1 = ["Name",raw_input("Enter Name : ").lower()]
        k2,v2 = ["Date",date.today()]
        k3,v3 = ["Address",raw_input("Enter your Address : ")]
        k4,v4 = ["City",raw_input("Enter city : ")]
        k5,v5 = ["State",raw_input("Enter State : ")]
        key = [k1,k2,k3,k4,k5]
        value = [v1,v2,v3,v4,v5]
        for i in range(5):
            dt = {key[i]:value[i]}
            i+=1
            lt.add(dt)
        stop = time.clock()
        print "\nTime Taken to ADD : {} sec".format(stop-start)

    elif ch == 2:
        os.system('cls')
        if len(lt.temp)==0:
            print "List is empty.'ADD' in the list first."
        else:
            lt.display()
            stop = time.clock()
            print "\nTime Taken to DISPLAY : {} sec".format(stop-start)

    elif ch == 3:
        os.system('cls')
        if len(lt.temp)==0:
            print "Nothing to Delete.'ADD' in the list first."
        else:
            name = raw_input("Enter Name of Customer :").lower()
            found = False
            ind = 0 # returns the index value for deletion
            for i in lt.temp:
                if i.values()[0] == name:
                    y_n = raw_input("Customer Present.Do you want to Delete Customer- Y/N : ").lower()
                    found = True
                    if y_n == 'y':
                        lt.delete(ind)
                ind +=1
            stop = time.clock()
            print "\nTime Taken to DELETE : {} sec".format(stop-start)

            if found == False:
                print "Customer not Found."

    elif ch == 4:
        os.system('cls')
        if len(lt.temp)==0:
            print "Nothing to SEARCH.'ADD' in the list first."
        else:
            s = input('1.Search by DATE   OR   2.search by Name : ')
            if s ==2:
                name = raw_input("Enter Name of Customer :").lower()
                found = False
                ind = 0
                for i in lt.temp:
                    if i.values()[0] == name:
                        print "Customer '{}' Found.".format(name)
                        found = True
                        stop = time.clock()
                        print "\nTime Taken to SEARCH : {} sec".format(stop-start)
                    ind +=1
                if found == False:
                    print "Customer '{}' not Found.".format(name)
                    stop = time.clock()
                    print "\nTime Taken to SEARCH : {} sec".format(stop-start)
            else:
                date = input("Enter Today's Date :")
                #today.month returns current month
                #today.year returns current year
                lt.search(date,today.month,today.year)

    elif ch==5:
        os.system('cls')
        if len(lt.main)==0:
            print "Nothing in Main List. 'ADD' in the list first."
        else:
            lt.mainList()

    elif ch==6:
        os.system('cls')
        if len(lt.temp)==0:
            print "Nothing in List. 'ADD' in the List first."
        else:
            lt.fileHandler(filename)
            print "Saved in file."

    else:
        os.system('cls')
        print "PROGRAM TERMINATED"
        break