a = input("Enter numerator:")
b = input("Enter denomenator:")
div = a/b
if div == 0:
    print "{}/{} = {}".format(a,b,div)
else:
    i = 0
    while i < 7:
        rem = (a%b)*10
        r_div = rem/b
        i+=1
    print "{}/{} = {}.{}".format(a,b,div,r_div)
