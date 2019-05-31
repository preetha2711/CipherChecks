file = open("prime_number.txt","r")

for line in file:
    p = int(line) 
    
    # p = int(input("Enter p"))

    Q = []
    for i in range(2, p):
        
        if ((p-1)%i == 0):
            Q.append(i)

    #q belongs in Q

    for g in range(2,761):
        flag = True
        for q in Q:
            if  (g**int((p-1)/q)) % p == 1:
                flag = False
                break
        if flag == True:
            print g

         

