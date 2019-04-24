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

def generate_primitive_root(p,q): #implement lucas test
    random_num = random.getrandbits(300)
    random_num |= (1 << 300 - 1) | 1
    num = p
    p = int(2)
    flag = False
    while (flag == False):
        cen = pow(random_num, int((num-1)/2), num )
        if (cen%num == 1):
            flag =  False 
        cen = pow(random_num,int((num-1)/q),num)
        if(cen%num==1):
            flag = False
        flag = True
        if flag == True:
            break
        random_num = random.getrandbits(300)
        random_num |= (1 << 300 - 1) | 1
    return random_num

#get stuff
p, q = get_two_primes()
g = generate_primitive_root(p,q)
g = pow(g,2,q)
a = random.randrange(2, (p-1))
h = pow(g,a, q)

#write stuff to files
file = open("public_key.txt", "w")
file.write(str(q) + "\n")
file.write(str(g) + "\n")
file.write(str(h))
f = open("private_key.txt","w")
f.write(str(a))

f_p = open("p_val.txt","w")
f_p.write(str(p))

public_key = (q,g,h)
secret_key = a