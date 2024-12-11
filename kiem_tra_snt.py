import math
import random

m = int(input("Nhap so (m<=3) m = "))

def Ghi_snt(m):
    U = [2,3]
    for i in range(4,m-1,1):
        kq = True
        for j in U:
            if (i%j==0): 
                kq = False
                break
        
        if (kq): U.append(i)
    return U    
    
def ktra_snt(n):
    k = int(math.sqrt(n))     
    if (n%2 == 0): return False
    for i in range(3,k,2):
        if (n%k == 0): return False
    return True

def Ghi_snt2(n):
    U = [2,3]
    for i in range(5,n-1,1):
        if (ktra_snt(i)): U.append(i)
        
    return U



    
    
def miller_rabin(n,t):
    if (n == 2) or (n == 3): return True
    if (n<=1) or (n%2 == 0): return False
    x = n -1 
    s = 0
    
    while(x%2==0):
        x = x//2
        s = s+1
        
    r = x
    
    for _ in range(t):
        a= random.randint(2,n-2)
        y = pow(a,r,n)
        
        while(y!=1) and (y!=n-1):
            j=1 
            while(j <= s-1) and (y != n-1):
                y = pow(y,2,n)
                if (y == 1): 
                    return False
                j = j + 1
            if y != n-1: 
                return False
    return True

if miller_rabin(997961,13): print("oke chay thanh cong")
else: print("oke fen")
                
        
#Kiem tra xem t co nho hon can hai cua n khum

def check_t(user_check_n):
    max_t = math.sqrt(user_check_n)
    while True:
        try:
            user_input_t = int(input(f"Nhap gia tri t (t <= {max_t}) "))
            if (user_input_t>0) and (user_input_t<max_t):
                print("Gia tri cua t la : ",user_input_t )
                break
            else:
                print("Hay Nhap dung gia tri!!")
        except ValueError:
            print("Hay nhap dung gia tri ")
            
    return user_input_t

#ghi vao so nguyen duong n

while True:
    try:
        user_input_n = int(input("Nhap so nguyen duong n (n nen >=3) : "))
        if (user_input_n>0):
            break
        else:
            print("Nhap dang hoang di cuuuuu!!!")
    except ValueError:
        print("Hay nhap dung gia tri nguyen duong")
        

t = check_t(user_input_n)

result = miller_rabin(user_input_n,t)

if result:
    print(user_input_n,"la so nguyen to")
else:
    print(user_input_n,"khong la so nguyen to")
    
    
    
#=================================================================

def Ham_kiem_tra(start,end,t):
    primes = [num for num in range(start,end + 1) if (miller_rabin(num,t))]
    return primes


while True:
    try:
        user_start = int(input("Nhap gia tri bat dau (n nen >=3) : "))
        if user_start >0:
            break
        else:
            print("Nhap lai di cuuuuuuuu!!!!")
    except ValueError:
        print("Nhap so nguyen duong di fen !")

while True:
    try:
        user_end = int(input("Nhap gia tri ket thuc di cu!!"))
        if user_end>user_start:
            break
        else:
            print("Nhap lai di cu (nho hon gia tri ban dau) ")
    except ValueError:
        print("Nhap so nguyen di cu!!")
        
t = check_t(user_end)

prime_numbers = Ham_kiem_tra(user_start,user_end,t)

print(f"Cac so nguyen to nam trong khoang {user_start} den {user_end} la : ",prime_numbers)