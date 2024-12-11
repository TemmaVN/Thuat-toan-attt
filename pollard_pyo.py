import math

def gcd_here(a,b):
    if (b==0): return a
    return gcd_here(b,a%b)

def pollard_rho(n):
    a = 2
    b = 2
    i = 0
    while i<1000:
        a = (a**2+1)%n
        b = (b**2+1)%n
        b = (b**2+1)%n
        
        if (a >b) :d = gcd_here(a-b,n)
        else: d = gcd_here(b-a,n)
        

        if (d>1) and (d<n): return d
        if (d==n):return -1
        i += 1
    return -1
    

print(pollard_rho(455459))