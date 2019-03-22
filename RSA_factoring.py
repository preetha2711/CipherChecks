
import fractions
import random as rn 

def factor(n,e,d):
    s=0
    t = e*d - 1

    while (t%2==0):
        s += 1
        t = t/2
    
    z_star_n = []
    for i in range(2, n+1):
        if fractions.gcd(i,n) == 1:
            z_star_n.append(i)

    b = 0
    flag = True
    while (flag == True):
        a = rn.choice(z_star_n)
        # temp = pow(a,t)
        b = pow(a,t,n)
        while (pow(b,2,n)) != 1:
            b = b*b%n
        if ((b%n!=1) and ((b+1)%n!=0)):
            flag = False

    p = fractions.gcd(b-1,n)
    q = n/p
    return(p,q)

print factor(1501,323,539)
