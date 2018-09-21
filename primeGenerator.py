
import random
def prime(check = None):
    
    if check == None:
        num = random.randint(1,10000)
    else:
        num = check

    prime_stat = True
    for i in range(2,num): # prime num can have 2 factors ' 1 and num itself'
        if num%i==0:
            prime_stat = False
            mul1 = i
            mul2 = num/i
            break

    # if prime_stat == False:
    #     print "{} is not prime because |{} X {} = {}|".format(num,mul1,mul2,num)
    # else:
    #     print "{} is prime num".format(num)

    if prime_stat == True:
        return num # returns None if not a prime

print prime(59)
