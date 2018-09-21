class Postfix:
    def __init__(self,capacity):
        self.top = 0
        self.capacity = capacity
        self.array = []

    def isEmpty(self):
        return True if (self.top) == 0 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -=1
            return self.array.pop()
        else:
            return "$"

    def push(self,op):
        self.top+=1
        self.array.append(op)

    def evaluate(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))

        return int(self.pop())

exp = "14+3-"
obj = Postfix(len(exp))
print "Value of {} is {}".format(exp,obj.evaluate(exp))