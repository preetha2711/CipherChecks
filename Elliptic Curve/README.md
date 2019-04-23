### Elliptical Curve Cryptography


1. Run "python EC.py"
2. All operations are inside relevant functions in the program. 
3. You need to type out whichever command you want to run in the program. 
4. Domain parameters are written in 'domainparameters'. This file consists of p, a and b values in that order
### Function definitions
 **read_EC_param()** 
 **check_EC(x,y)** - Checks if the given points x and y lie on the EC given in 'domainparameters'
 **read_EC_point()** - Prompts user to enter point through the command line
 **write_EC_point()** - Prints point to command line
 **add_EC(x1,y1,x2,y2)** - Adds (x1,y1) and (x2,y2)
 **subtract_EC(x1,y1,x2,y2)** - Subtracts (x2,y2) from (x1,y1)
 **multiply_EC(k, x1, y1)** - Multiplies (x1,y1) k times
 **neg_EC(x1,y1)** - Gives the negation of a given point x1,y1
 **return_EC_pt(x)** - Implements Shanks algo to return the y coordinate of a given x, on the EC.

Collaborators : Vineet Reddy
