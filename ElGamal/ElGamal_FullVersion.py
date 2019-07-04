import random
import math
import sys
sys.setrecursionlimit(100000)

def miller_rabin(number): #checks whether number is prime or not
    B = False
    num_1 = number - 1
    k = 0
    while(num_1 % 2 == 1 ):
        num_1 = num_1/2
        k += 1 
    m = num_1//(2**k)
    a = random.randint(0,num_1)
    b = pow(a,m,number)
    if b == 1 : 
        B = True
    else :
        for i in range(k):
            if b % n == -1:
                B = True
            else :
                b = pow(b,2,number)        
    return B


def generate_prime(length = 300): #this generates primes of the given bit length
    flag = False
    while(flag != True):
        # generate random bits
        random_num = random.getrandbits(length)
        # apply a mask to set MSB and LSB to 1
        random_num |= (1 << length - 1) | 1
        flag = miller_rabin(random_num) #probabilistically try Miller Rabin
        prime_number = random_num
        return prime_number
        

def get_two_primes():
    flag = False
    while (flag != True):
        p = generate_prime()
        q = 2*p + 1 
        flag = miller_rabin(q)
    return p,q #q = 2p + 1

def lucas_test(integer):
    p = integer
    Q = []
    for i in range(2, p):    
        if ((p-1)%i == 0):
            Q.append(i)
    #q belongs in Q
    prim_roots = []
    for g in range(2,p):
        flag = True
        for q in Q:
            if  (g**int((p-1)/q)) % p == 1:
                flag = False
                break
        if flag == True:
            # print g
            prim_roots.append(g)
    return(prim_roots)

p, q = get_two_primes()

# prim_roots = lucas_test(int(q))

# g = random.choice(prim_roots)

# g = g^2 % q

# a = random.randrange(2,(p-1)) #Secret key

# h = pow(g,a,q)

# print q, g, h


