
file = open("cipher.txt","r")
f_write = open("possible_answers.txt","w")
content = file.read()
array = [str(content)]
array = ['hgnodxnthmsdqbdossghrrdbqdssqzmrlhrrhnmvhsgntszmxdqqnqsghrsqz mrlhrrhnmgzrsqzudkkdczlhkkhnmkhfgsxdzqrsnhmenqlxntsgzsvdzqdbn lhmfrnnm']
ciphertxt = []
for i in range(0,len(array[0])):
    ciphertxt.append(array[0][i])
letter_num = {}
for i in range(97,123):
     letter_num[(i-97)] = chr(i)

#the letter_num array format is as follows : 
#0:a,1:b, 2:c...


#making the shift cipher

def shift_cipher(string):
    poss_ans = []
    for i in range(26):
        temp_str = ''
        for j in string:
            # print j
            temp_chr = letter_num[((int(ord(j)) - 97 + i)%26)]
            temp_str += temp_chr
        # print i
        poss_ans.append(temp_str)

    return poss_ans
possible_answers = shift_cipher(array[0])
f_write.write(str(possible_answers))
 