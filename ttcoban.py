import math

# Ví dụ:
#F = 2147483647
#W = 8 # bội số của 8, độ rộng của từng phần tử trong mảng 
#a = 23456789

def so_sang_mang(F,W,a):
    List = []
    m = math.ceil(math.log2(F))
    t = math.ceil(m/W)
    print(m,t)
    
    for i in range(0,t):
        x = 2**((t-i-1)*W)
        b = a//x
        a = a%x
        List.append(b)
    
    return List

def mang_sang_so(F,W,List):
    kq = 0
    m = math.ceil(math.log2(F))
    t = math.ceil(m/W)
    
    for i in range(t):
        x = 2**((t-i-1)*W)
        kq += List[i]*x
        
    return kq

#print(mang_sang_so(2147483647,8,[0, 1, 226, 64]))
    
    