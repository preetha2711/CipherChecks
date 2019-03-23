from random import randrange, getrandbits
import math
import random

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

#using miller Rabin to generate prime numbers of 1024 bit length
p = (generate_prime_number(1024))
q = (generate_prime_number(1024))
print (p)
n = p*q
phi_n = (p-1)*(q-1)

flag = True
while (flag == True):
    e = random.randint(2,phi_n)
    if (math.gcd(e, phi_n) != 1):
        flag = True 
    else : 
        flag = False




# #"by God's grace" - PK, 2019

def extended_euclidian_algo(a,b):
    s = 0
    t = -1 
    old_s = 1
    old_t = 0
    r = b
    old_r = a

    while(r!=0):

        q = old_r//r

        old_r, r = r, (old_r - (q*r))
        old_s, s = s, (old_s - (q*s))
        old_t, t = t, (old_t - (q*t))

    return(old_s,old_t)
d, k = (extended_euclidian_algo(e,phi_n))
file = open("public_key.txt", "w")
file.write(str(e))
file.write(('\n'))
file.write(str(n))

f = open("private_key.txt", "w")
f.write(str(d%n))
print("d",d)


print ("""""""")


