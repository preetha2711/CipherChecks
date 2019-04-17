def lucas_test(integer):
    p = integer

    Q = []
    for i in range(2, p):
        
        if ((p-1)%i == 0):
            Q.append(i)

    #q belongs in Q
    prim_roots = []
    for g in range(2,p):
        flag = True
        for q in Q:
            if  (g**int((p-1)/q)) % p == 1:
                flag = False
                break
        if flag == True:
            # print g
            prim_roots.append(g)

    return(prim_roots)


print lucas_test(761)
         

