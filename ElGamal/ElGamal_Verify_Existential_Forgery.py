file = open("public_key.txt", 'r')
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()

file = open("forged_sign.txt",'r')
r = int(file.readline())
signature = int(file.readline())
file.close()

file = open("plain_text_forgery.txt", 'r')
plain_text_forgery = int(file.readline())
file.close()

g_m = pow(g,plain_text_forgery,q)
rhs = (pow(h,r,q)*pow(r,signature,q))%q
if(g_m == rhs):
    print("True")
else:
    print("False")