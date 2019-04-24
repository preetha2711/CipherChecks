import hashlib

file = open("plain_text.txt","r")
plain_text = file.read()
hashed_text = hashlib.sha256(plain_text).hexdigest()
file.close()

f_write = open("plain_text.txt", "w")
f_write.write(str(hashed_text))