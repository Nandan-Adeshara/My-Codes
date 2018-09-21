import os,time

class Dictionary:
    ''' Contains methods and functions for Dictionary'''
    def __init__(self,file):
        self.list    = []
        self.filename= file
    
    def add(self,key,value):
        dict1 = {key:value}        
        self.list.append(dict1)
        return self.list

    def updatekey(self,index,old,new):
        self.list[index-1][new] = self.list[index-1].pop(old)
        return self.list

    def updateword(self,index,key,value):
        self.list[index-1][key].extend(value)
        return self.list

    def updatevalue(self,index,olValue,upValue):
        v = self.list[index-1].values()
        ind_val = v[0].index(olValue)
        self.list[index-1].values()[0][ind_val] = upValue 
        return self.list

    def deleteitem(self,index):
        self.list.pop(index-1)
        return self.list
        
    def deletevalue(self,index,value):
        ind_val = self.list[index-1].values()[0].index(value)
        del self.list[index-1].values()[0][ind_val]

    def file(self,key,value):
        dict_list = []
        dict_list.extend(key)
        dict_list.extend(value)
        ind = 0
        f = open(self.filename,'w')
        f.write("Dictionary: \n")
        for i in key:
            f.write("\n")
            f.write(i)
            f.write("-\n")
            for j in value[ind]:
               f.write(j)
               f.write(",")
            ind+=1
        f.close()
           
    def __str__(self):
        return "Dictionary is ",self.dict                         

os.system('cls')
file = 'dictionary.txt' 
dt = Dictionary(file)
while True:
    print "-"*30,"\nWord Dictionary Options:-\n1.ADD \n2.UPDATE \n3.DELETE \n4.SEARCH \n5.DISPLAY 'DICTIONARY' \n6.SAVE in the FILE\n7.EXIT\n","-"*30
    choice = input("Select from above options:")
    
    if choice==1:
        key,value = [raw_input("input a key for a new dict:"),raw_input("input all the words(comma separated) for the given key:").split(",")]
        dt.add(key,value)
        print "\n\"Addition successful\""
                        
    elif choice==2:
        if len(dt.list)==0:
            os.system('cls')
            print "Nothing in dictionary.'ADD' a dictionary first"
        else:
            print 'Below is the Dictionary for updation-\n',dt.list
            opt = input('\nSelect:1.Update key  OR  2.Update value of a particular key\n-->:')
            if opt==1:
                i = 1
                print "Keys are:"           
                for dct in dt.list:
                    print i,"=",dct.keys()[0]
                    i+=1  
                keyNo,oldK,newK = [input("Num:"),raw_input("old key:"),raw_input("new key:")]    
                dt.updatekey(keyNo,oldK,newK)
                print "\n\"Key Update Successful\"" #(if i dont mention this statement it will not exit out of the loop)

            else:
                i = 1
                print "Dictionary is:"
                for dct in dt.list:
                    print str(i) + ".",dct.keys()[0],"=",dct.values()[0]
                    i+=1
                choice = input("\nSelect:1.Add more words OR 2.Update value\n-->")
                if choice == 1 or choice ==2:
                    num,key,value = input("Num : "),raw_input("Key : "),raw_input("Value/s : ").split(",")
                if choice == 1:
                    dt.updateword(num,key,value) # 1st index coz it is a list and in method it identifies a str
                    os.system('cls')
                    print "\n\"Words Added Successful\""
                elif choice==2:
                    chge_value = raw_input("New Value : ")
                    dt.updatevalue(num,value[0],chge_value) 
                    print "\n\"Value updation Successful\"" 
            
    elif choice==3:
        if len(dt.list) == 0:
            os.system('cls')
            print "Nothing to Delete. 'ADD' first"
        else:
            i = 1
            for dct in dt.list:
                print str(i) + ".",dct.keys()[0],"=",dct.values()[0]
                i+=1
            opt = input("\nSelect:1.Delete a whole item OR 2.Delete a value of a key\n-->")
            if opt == 1:
                num = input("Num:")
                dt.deleteitem(num)
                print "\n\"Key Successfully Deleted\""
            else:
                num,val = [input("Num : "),raw_input("Value : ")]
                dt.deletevalue(num,val)    
                print "\n\"Value Successfully Deleted\""

    elif choice==4:
        if len(dt.list) == 0:
            os.system('cls')
            print "Nothing to Search. 'ADD' first"
        else:
            opt = input("1.Search by Key  OR  2.Search by Value\n-->")
            start = time.clock()
            found = False
            if opt ==1:
                k = raw_input("Search Key : ").lower()
                for i in dt.list:
                    if i.keys()[0].lower() == k:
                        print "\nKey '{}' is present in dictionary.".format(k)
                        found = True
                if found == False:
                    print "Key '{}' not present".format(k)
                elapsed = time.clock()
                elapsed = elapsed - start
                print "\nTime spent to 'SEARCH Key' is : %d ms"%elapsed    

            else:
                v = raw_input("Search Value : ")
                for i in dt.list:
                    for j in i.values():
                        ind = 1
                        for val in j:
                            if v == val:
                                print "\nValue '{}' found at '{}' position in Dictionary".format(v,ind)
                                found = True
                            else:    
                                ind+=1

                elapsed = time.clock()
                elapsed = elapsed - start
                print "\nTime spent to 'SEARCH Value' is : %d ms"%elapsed

            if found == False:
                print "\nValue '{}' not present in Dictionary".format(v)        
                      
    elif choice==5:
        if len(dt.list)==0:
            os.system('cls')
            print "Empty Dictionary. 'ADD' first."
        else:
            os.system('cls')
            i=1    
            for dct in dt.list:
                print str(i) + ". ", dct.keys()[0], "=", dct.values()[0]
                i+=1

    elif choice==6:
        if len(dt.list)==0:
            os.system('cls')
            print "Empty Dictionary. 'ADD' first."
        else:
            key = []
            value = []
            for dct in dt.list:
                key.append(dct.keys()[0])
                value.append(dct.values()[0])   
            print value
            dt.file(key,value)
            os.system('cls')
            print "Saved in file '{}'".format(file)

    else:
        os.system('cls')
        print "Program Terminated"
        break