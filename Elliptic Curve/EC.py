def read_EC_param():

    file = open("domainpoints.txt", "r")
    data = file.read()
    data = data.split(" ")
    p = data[0]
    a = data[1]
    b = data[2]
    p = int(p)
    a = int(a)
    b = int(b)
    return p,a,b


def check_EC(x,y): #function to check if given co-ordinates are part of EC or not
    # p,a,b = read_EC_param()    
    return ((y**2 - (x**3 + a*x + b)) % p == 0 and 0 <= x < p and 0 <= y < p)


def inv_mod(x):
    if x % p == 0 :
       return ("Inverse does not exist ")
    return pow(x,p-2,p)


def read_EC_point():
    x = int(raw_input("enter x "))
    y = int(raw_input("enter y "))

    return x,y

p,a,b = 59,17,5

def add_EC(x1,y1,x2,y2):    
    if (x1 == 0 and y1 == 0 ): #ie one of the points is Origin
        return x2, y2
    elif (x2 == 0 and y2 == 0): #if the second pt is 0,0
        return x1, y1
    elif (( y1 == ((-1)*y2 % p) ) and (x2 == x1)): #one of the pts is inverse of the other
        return 0,0 
    else : 
        if ((x1 == x2) and (y1 == y2)): #if they're the same pts
            slope = (3*x1*x1 + a) * inv_mod(2 * y1) #same slope as in point doubling
        else : 
            slope = (y2-y1) * inv_mod(x2 - x1)
    x_new = (pow(slope,2) - x1 - x2)%p
    y_new = (slope * (x1-x_new) - y1)%p
    return (x_new, y_new)

def subtract_EC(x1,y1,x2,y2): #add the inverse of the point
    y2 = (y2 * -1) % p
    x_sub,y_sub = add_EC(x1,y1,x2,y2)
    return x_sub, y_sub

def multiply_EC(k, x1,y1): #use the point doubling method
    slope = (3*x1*x1 + a) * inv_mod(2 * y1) #pt doubling method
    x_new = (pow(slope,2) - x1 - x1)%p
    y_new = (slope * (x1-x_new) - y1)%p

    for i in range(0,k-2):
        x_new, y_new = add_EC(x1,y1,x_new, y_new) #simple addition   
    return x_new,y_new


print add_EC(8,2,8,2)
for i in range(0,1000):
    print i
    print multiply_EC(i,8,2)


