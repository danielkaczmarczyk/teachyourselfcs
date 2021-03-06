"""
Give a signed 32-bit integer x, return x with its digites reversed. If 
reversing x causes the value to go outside the signed 32-bit integer
range [-2^31, 2^31 - 1], then return 0

Assume the environment does not allow you to store
64-bit integers (signed or unsigned)
"""

def reverse_integer(x):
    reversed_int = ''
    
    while x > 0:
        reversed_int += str(x % 10)
        x //= 10

    print(reversed_int)



reverse_integer(123)
