import random
import math
import binascii



file = open("public_key.txt", 'r')
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()

f_p = open("p_val.txt", 'r')
p = int(f_p.readline())

f = open("private_key.txt","r")
a = int(f.readline())

f_message = open("plain_text.txt", "r")
plain_text = f_message.read()


encrypted_text = int(binascii.hexlify(plain_text.encode('utf-8')),16)

k = random.randrange(2, (p-1))

r = pow(g,k,q)

#memory credits : Paul Kurian, da best
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

old_s, old_t = extended_euclidian_algo(k,p)
inv = old_s % p
sign = (encrypted_text - a*r)%p

sign = (sign * inv) % p

file = open("sign.txt", 'w')
file.write(str(r) + "\n")
file.write(str(sign) + "\n")



