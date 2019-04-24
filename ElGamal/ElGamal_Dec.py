import math 
import binascii


file = open("public_key.txt", 'r')
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())
for line in file : 
    line = file.read()
file.close()

f_sign = open("sign.txt",'r')
r = int(f_sign.readline())
signature = int(f_sign.readline())
f_sign.close()

f_plain = open("plain_text.txt", 'r')
plain_text = f_plain.read()
message_Encrypted = int(binascii.hexlify(plain_text),16)



g_m = pow(g,message_Encrypted,q)
rhs = (pow(h,r,q)*pow(r,signature,q))%q
if(g_m == rhs):
    print("True")
else:
    print("False")


