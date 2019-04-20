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
    p,a,b = read_EC_param()
    
    return ((y**2 - (x**3 + a*x + b)) % p == 0 and 0 <= x < p and 0 <= y < p)
print check_EC(4,14)
print check_EC(8,2)

def inv_mod(x):
    if x % p == 0 :
       return ("Inverse does not exist")
    return pow(x,p-2,p)

def neg_pts_EC(x1,y1):
    y1 = (y1 * -1) % p
    return x1, y1

def read_EC_point():
    x = int(raw_input("enter x"))
    y = int(raw_input("enter y"))

    return x,y


p,a,b = read_EC_param()
x1,y1 = read_EC_point()
x2,y2 = read_EC_point()

# print inv_mod(x2-x1)
def add_EC(x1,y1,x2,y2):
    ##ADD CORNER CASES##
    if (y2 - y1 % p == 0 ):
        return 0

    slope = ((y2-y1) * inv_mod(x2 - x1)) % p
    print "slope is " , slope
    x_new = (pow(slope,2) - x1 - x2)%p
    y_new = (slope*(x1-x_new) - x2)%p

    return (x_new, y_new)

print add_EC(x1,y1,x2,y2)

def subtract_EC(x1,y1,x2,y2):
    x2,y2 = neg_pts_EC(x2,y2)
    x_sub,y_sub = add_EC(x1,y1,x2,y2)

    return x_sub, y_sub





