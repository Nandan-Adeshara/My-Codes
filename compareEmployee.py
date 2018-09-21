''' compare employees Salary'''

import os
class Person:    
    def __init__(self):
        self.name = ''
        self.age = None
        self.address = ''
        self.email = ''
        self.contact = None
        
    def __str__(self):
        return self.name
        return self.age
        return self.address
        return self.email
        return self.contact
        
    def Input(self):
        self.name = raw_input("Enter your name:")
        self.age = input("Enter your age:")
        self.address = raw_input("Enter your address:")
        self.email = raw_input("Enter your email:")
        self.contact = input("Enter your contact:")

    def Display(self):
        #Employee.Input()        
        print '.'*30
        print "Employee Details-"
        print "  Name of employee is",self.name
        print " ",self.name+"'s age is",self.age
        print " ",self.name+"'s address is",self.address
        print " ",self.name+"'s email is",self.email
        print " ",str(self.name)+"'s contact is",self.contact
        
class Employee(Person):
    
    def __init__(self):
        Person.__init__(self)
        self.empid = None
        self.designation = ''
        self.department = ''
        self.salary = None
        
    def __str__(self):
        return Person.__str__(self)
        return str(self.empid)
        return self.designation
        return self.department
        return str(self.salary)
    
    def Input(self):
        try:
            #super().Input()
            Person.Input(self)
            self.empid = input("Enter your ID:")
            self.designation = raw_input("Enter your designation:")
            self.department = raw_input("Enter your Department:")
            self.salary = input("Enter your salary:")
            #return self
        except:
            os.system("cls")
            print "some error...Give Input Accordingly"
            return emp.Input()
            
    def Display(self):
        os.system("cls")
        Person.Display(self)
        print " ",str(self.name)+"'s ID is",self.empid
        print " ",self.name+"'s designation is",self.designation
        print " ",self.name+"'s Department is",self.department
        print " ",str(self.name)+"'s salary is",self.salary    
        print '.'*30    
        

emp = Employee()
emp_obj = []
while True:
    print "-"*20
    print "1.Add Employee \n2.Display Emoloyee \n3.Compare Employee \n4.Exit"
    print "-"*20
    choice=input("Enter your choice by selecting the option number:")
    if choice == 1:
        os.system("cls")
        emp_obj.append(Employee().Input())
    elif choice == 2:
        os.system("cls")
        print "Sr.Num\tName\t\tAge\tAddress\t\tE-mail\t\t\tContact\t\tEmpID\t\tDesignation\t\tDepartment\tSalary"
        i=1
        for s in  emp_obj:
            print i,"\t",s.name ,"\t",s.age,"\t",s.address,"\t",s.email,"\t",s.contact,"\t",s.empid,"\t\t",s.designation,"\t\t",s.department,"\t\t",s.salary
            i+=1
    elif choice == 3:
        os.system("cls")
        print "Will specify-\n 1.Greater than the specified amount\n 2.Lesser than the specified amount"
        sal=input("Enter the specify amount:")
        print "Name\tSalary\tInfo"
        for user in emp_obj:
            if sal <= user.salary:
                print user.name,"\t",user.salary,"Employee is having Greater salary than specified"
            else:
                print user.name,"\t",user.salary,"Employee is having Lesser salary than specified"
    else:
        os.system("cls")
        break                    
