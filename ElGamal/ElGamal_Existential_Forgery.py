import random

file = open("public_key.txt", "r")
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()

f_p = open("p_val.txt", 'r')
p = int(f_p.readline())

z = random.randrange(2, (p-1))
r = pow(g,z,q)
r = (r*h) % q
s = (-r)%p
m = (z*s)%p

f_write = open ("forged_sign.txt", "w")
f_write.write(str(r) + "\n")
f_write.write(str(s) + "\n")

file = open("plain_text_forgery.txt", 'w')
file.write(str(m) + "\n")

