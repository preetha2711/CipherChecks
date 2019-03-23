file = open("public_key.txt","r")
keys = []
for line in file:
    keys.append(int(line))
    
e = keys[0]
n = keys[1]

f = open("plaintext.txt","r")
for line in f:
    plaintext = int(line)
print (plaintext)
print (e)
print (n)
c = pow(plaintext,e,n)

file_open = open("ciphertext.txt", "w")
file_open.write(str(c))