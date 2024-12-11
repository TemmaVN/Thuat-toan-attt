import math

def eratosthenes(n):
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    
    p=2
    
    while p**2<=n:
        if (primes[p]==True):
            for i in range(p**2,n+1,p):
                primes[i] = False
                
        p+=1
    
    primes_num = [i for i in range(n) if primes[i]]
    
    return primes_num

while True:
    try:
        n = int(input("Nhap so nguyen duong n = "))
        if (n>0):
            break
        else:
            print("Hay nhap 1 so nguyen duong !! ")
    except ValueError:
        print("Hay nhap 1 so nguyen duong !! ")
        
print(f"Cac so nguyen to be hon {n} la ", eratosthenes(n))



             
     