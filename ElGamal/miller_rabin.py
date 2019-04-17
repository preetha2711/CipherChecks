import random
def miller_rabin(number):

    B = False

    num_1 = number - 1
    k = 0

    while(num_1 % 2 == 1 ):
        num_1 = num_1/2
        k += 1 
    m = num_1/ (2**k)

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


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = random.getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
# for i in range(100):
#     prime = generate_prime_candidate(300)    
#     print miller_rabin(prime)
#     if miller_rabin(prime):
#         print "FUCK YES THIS WORKS"
