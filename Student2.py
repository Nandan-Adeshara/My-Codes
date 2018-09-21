class Student:
    ''' class Student with some info and perform operations'''
    def __init__(self):
        self.name=None
        self.rollNo= None
        
    def Input(self):
        self.name=str(raw_input("Enter Name:"))
        self.rollNo=int(input("Enter Roll number:"))
        return self
        
        
    def Display(self):
        print ("Name of student is :"+ self.name)
        print ("Roll Number of " + self.name + " is :" + str(self.rollNo))
        
    def clearAll(self):
        del self.name
        del self.rollNo
        
if __name__=='__main__':
    std_obj=[]
    while True:
        #print dir(student)
        print ("*"*50)
        print (" 1. Add Students \n 2. List all students \n 3. Search student by name \n 4. Total number of student added \n 5. Exit") 
        print ("*"*50)
        choice=input("Enter your choice from above:")
                

        if choice==1:
            
            std_obj.append(Student().Input())
        elif choice==2:
            print "*"*15
            print "List of all the objects:"        
            print "SN\tName\t\tRollNo."
            i=1
            for s in std_obj:
                print  i,"\t",  s.name,"\t\t", s.rollNo
                i+=1
                
        elif choice==3:
            print "Search student by name-"
            name= str(raw_input("\nEnter Student's name:"))
            for s in std_obj:
                if s.name==name:
                    print "Student  found"
                else:
                    print "Student   not found"
                    
        elif choice==4:        
            count =len(std_obj)
            print "Total Num of Students added are: " + str(count)
            
        else:
            Student().clearAll()
            break