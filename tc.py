import os,getpass,time,random

class User:
    ''' Takes details of users.
        Ticket distribution and QR ID generation.
        Display History.
    '''
    def __init__(self):
        self.fname   = None
        self.lname   = None
        self.name    = None
        self.gender  = None
        self.age     = None
        self.pw      = None
        self.seat    = 2  # total seats
        self.src     = None
        self.dest    = None
        self.confirm = False
        self.detail  = []
        self.ticket  = []
        self.conf_ticket  = []
        self.finalStatus = []
         
    def signUp(self):
        os.system('cls')
        self.fname,self.lname = raw_input("Enter First name : ").lower(),raw_input("Enter last name : ").lower()
        self.name   = self.fname + ' ' + self.lname
        self.age    = input("Enter age : ")
        self.gender = raw_input("Enter Gender : ").lower()
        self.pw     = getpass.getpass("Password:: ")
        lt = [self.fname,self.lname,self.age,self.gender]
        
        self.detail.append(lt)
        os.system("cls")
        print "Please Login again"
        
    def login(self,user_f,user_l):
        os.system('cls')
        ind = 0
        found = False
        for i in self.detail:
            if i[0] == user_f and i[1] == user_l: # in login password can be used instead of last name. than the index of it will be given as per it's position in self.detail
                found =True
                print ":Correct Credentials:"
                s = raw_input("Do you want to Book Ticket (Y/N) : ").lower()
                if s == 'y':
                    self.bookTicket(ind)
                else:
                    print ":Successfully Logged Out:"
                    break
            ind+=1
        return found

    def bookTicket(self,ind):
        src = ['pune','amdavad','mumbai','delhi','bangaluru']
        dest = ['pune','amdavad','surat','delhi','punjab','udaipur','mumbai']

        self.src  = raw_input("Enter source : ")
        while self.src not in src:
            print "Route to '{}' not available".format(self.src)
            self.src  = raw_input("Enter new source : ")

        self.dest = raw_input("Enter destination : ")
        while self.dest not in src:
            print "Route to '{}' not available".format(self.dest)
            self.dest  = raw_input("Enter new source : ")
        
        self.date = raw_input("Enter Date : ")
        lt = [self.src,self.dest,self.date]

        self.detail[ind].extend(lt)
        self.ticket.append(self.detail.pop(ind))
        self.confirmTicket()
            
    def confirmTicket(self): #ticket distributing algo
        ind = 0
        found = False
        print "Preparing Confirmed Ticket List..."
        time.sleep(1)
        if self.seat > 0:
            for i in self.ticket:
                if i[2]>60:  # ticket priority on basis of age
                    self.seat-=1
                    self.conf_ticket.append(self.ticket.pop(ind))
                    found = True
                    break
                elif i[3] == 'female' and i[2]>40: # ticket priority on basis of gender and age
                    self.seat-=1
                    self.conf_ticket.append(self.ticket.pop(ind))
                    found = True
                elif i[3] == 'male' and i[2] > 50:
                    self.seat -=1
                    self.conf_ticket.append(self.ticket.pop(ind))
                    found = True
                else:
                    print "'{}'".format(self.ticket[ind][0]),"wait till the next list comes."
                ind+=1
        else:
            os.system('cls')
            print "SORRY {} , No Seats Available!!".format(self.ticket[ind][0])

        if found == True:
            sel = raw_input("Press 'Y' to see and generate QR for your ticket : ").lower()
            if sel == 'y':
                self.generateQR()
            else:
                exit
            
    def generateQR(self):
        self.finalStatus
        ind = 0
        for i in self.conf_ticket:
            fare = str(random.randint(500,2000))
            qr = str(random.randint(10,99))
            l = i[0][0:2]+i[1][0:2] + qr
            self.conf_ticket[ind].append(fare)
            self.conf_ticket[ind].append(l)
            self.finalStatus.append(self.conf_ticket.pop(ind))
            ind+=1

        os.system('cls')
        print "Final Confirmed list is available with the Admin."
        
    def display(self):
        print "Final Confirmed List:"
        print "-"*20
        ind = 1
        if len(self.finalStatus) == 0 :
            print "List Empty."
        else:                
            for i in self.finalStatus:
                print "\nCustomer {}--".format(ind)
                print "FirstName   : ",i[0]
                print "LastName    : ",i[1]
                print "Age         : ",i[2]
                print "Gender      : ",i[3]
                print "Source      : ",i[4]
                print "Destination : ",i[5]
                print "Date        : ",i[6]
                print "Fare        :  Rs",i[7]
                print "QR ID       : ",i[8]
                ind+=1
        print "-"*20

    def checkName(self):
        if len(self.finalStatus)==0:
            print "List empty."
        else:
            f_name,l_name = raw_input("Ask Firstname : "),raw_input("Ask Lastname : ")
            found = False
            for i in self.finalStatus:
                if i[0] == f_name and i[1] == l_name:
                    found = True
                    os.system('cls')
                    print "{} {}'s ticket is confirmed.".format(f_name,l_name)
            if found == False:
                os.system('cls')
                print "{} {}'s ticket is not confirmed.".format(f_name,l_name)

    def checkID(self):
        ID = raw_input("Ask for QR ID  : ")
        found = False
        for i in self.finalStatus:
            if i[8] == ID:
                found = True
                os.system('cls')
                print i[0],"'s Ticket is confirmed."
        if found == False:
            os.system('cls')
            print "Ticket is not confirmed."

def userFunc(user):
    print "*"*10,"\n1.SignUp \n2.Login\n","*"*10
    opt = input("Select (1/2) : ")
    os.system('cls')
    if opt not in [1,2]:
        print "Select from 1 OR 2"
        userFunc(user)
    elif opt == 1:
        user.signUp()
    elif opt == 2:
        if len(user.detail)>0:
            print "To Login, provide-\n"
            user_f = raw_input("First name : ").lower()
            user_l = raw_input("Last  name : ").lower()
            if user.login(user_f,user_l) == False:
                opt = input(":Wrong Credentials:\n1.SignUp Instead  OR  2.Try again  OR  3. Exit\n> ")
                if opt == 1:
                    user.signUp()
                elif opt == 2:
                    user_f = raw_input("First name : ").lower()
                    user_l= raw_input("Last name : ").lower()
                    user.login(user_f,user_l)
                else:
                    exit
        else:
            print "LOGIN FIRST --"
            user.signUp()

def adminFunc(user):
    print "*"*30,"\n1.Search Passenger \n2.Display Final Confirmed List\n","*"*30
    opt = input("Select (1/2) : ")
    os.system('cls')
    if opt not in [1,2]:
        print "Select from:"
        adminFunc(user)
    elif opt ==1:
        user.checkName()
    elif opt ==2:
        user.display()

def tcFunc(user):
    print "-"*30,"\nCheck Passenger's Ticket by -\n1.Name  OR  2.QR ID\n","-"*30
    opt = input("Select (1/2) : ")
    os.system('cls')
    if opt not in [1,2]:
        print "Select from:"
        tcFunc(user)
    elif opt ==1:
        user.checkName()
    elif opt ==2:
        user.checkID()

# Object creation
os.system('cls')   
user  = User()
while True:
    print "*"*10,"\n1.ADMIN \n2.USER \n3.TC\n4.EXIT \n","*"*10         
    opt = input("Select : ")
    os.system('cls')
    if opt == 1:
        adminFunc(user)
    elif opt == 2:
        userFunc(user)
    elif opt == 3:
        tcFunc(user)        
    else:
        print ":Successful Termination:"
        break