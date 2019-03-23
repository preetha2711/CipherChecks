file = open("ciphertext.txt", "r")
file_1 = open("public_key.txt", "r")
file_2 = open("private_key.txt", "r")
public_key = []
for line in file_1:
    public_key.append(int(line))

e = public_key[0] 
n = public_key[1]

for line in file_2:
    d = int(line)

for line in file: 
    c = int(line)

m = pow(c,d,n)

print(m)