def gcd(a,b):
    while(b!=0):
        a,b = b,a%b
    return a

print(gcd(12,8))    
    
def extended_gcd(a,b):
    if (b==0): 
        return (a,0,1)
    else:
        (kq,u,v) = extended_gcd(b,a%b)
        return (kq,v - (a//b)*u,u)
    
    
print(extended_gcd(12,8))
