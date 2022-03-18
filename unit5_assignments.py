# Import square root function for Assignment 2
from math import sqrt

# Assignment 1. Checks the number and returns 'True' if it is even, or 'False' if it is not
def is_even(num):
    return (num % 2 == 0)

# Assignment 2. Solves quadratic equation for a, b, and c
# Returns one or two solutions, or nothing is returned if no solution is possible
def solve_quadratic(a, b, c):
    if a == 0:
        return None
    
    # Calculating discriminant, and if it is less than 0 the equation has no solution
    discriminant = (b * b) - (4 * a * c)
    if discriminant < 0:
       return None
    
    # Calculating two possible solutions
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)

    # If the two solutions are the same - return just one, if not - return both
    if x1 == x2:
        return x1
    else:
        return (x1, x2)
