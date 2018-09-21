class Student:

    def __init__(self):
        self.name=None
        self.rollno=None
        self.age=None
        self.mark1=None
        self.mark2=None
        self.mark3=None
        
    def Input(self):
        self.name=str(raw_input("Enter your name:"))
        self.rollno=int(raw_input("Enter your rollno:"))
        self.age=int(raw_input("Enter your age:"))
        self.mark1=float(raw_input("Enter marks for 1st subject out of 100:"))
        while self.mark1>100:
            self.mark1=float(raw_input("Sorry,Enter marks for 1st subject out of 100:"))
        else :
            None
        
        self.mark2=float(raw_input("Enter marks for 2nd subject out of 100:"))
        while self.mark2>100:
            self.mark2=float(raw_input("Sorry,Enter marks for 2nd subject out of 100:"))
        else :
            None
        
        self.mark3=float(raw_input("Enter marks for 3rd subject out of 80:"))
        while self.mark3>80:
            self.mark3=float(raw_input("Sorry,Enter marks for 3rd subject out of 80:"))
        else:
            None
        return self
        
    def Display(self):
        print "Name of student is",str(self.name)
        print "Roll number of",str(self.name),"is",self.rollno
        print self.name+"'s age is "+ str(self.age)
        print self.name+"'s marks are- \n for subject 1: "+str(int(self.mark1))+ "/100\n for subject 2: "+str(int(self.mark2)) +"/100\n for subject 3: " +str(int(self.mark3))+"/80"

    
    def Totalmark(self):
        calc=(self.mark1+self.mark2+self.mark3)
        print "Total marks of",self.name,"is",str(int(calc))+"/280"

    def Totalmarks(self):
        calc=(self.mark1+self.mark2+self.mark3)
        print str(int(calc))     

std_obj=[]
while True:
    a=raw_input("Write 'add' if want to add student:")
    student=Student()
    while a=="add":
        std_obj.append(student.Input())
        print "*"*20
        student.Display()
        student.Totalmark()
        print "--"*20
        print "\nS.No\tName\tRollNo.\tAge\tMark1\tMark2\tMark3\tTotalmarks"
        i=1
        for s in std_obj:
            print i,"\t",s.name,"\t",s.rollno,"\t",s.age,"\t",s.mark1,"\t",s.mark2,"\t",s.mark3,"\t",s.Totalmarks()
            i+=1
        print "--"*20
        break
    else:
        None
    print "if want to print number of student write '1'\nif want to print top 3 students with highest marks, write '2'"
    choice=input("Enter your choice:")

    if choice==1:
        print "Total no. of students are",len(std_obj)
    