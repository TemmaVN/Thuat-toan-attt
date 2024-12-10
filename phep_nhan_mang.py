import math

def phep_nhan_mang(A,B,t,W):
    C = [0]*(2*t)
    def dao_mang(D):
        return D[::-1]
    
    def Chuyen_sang_UV(number,W):
        binary_string = format(number,f'0{2*W}b')
        U = int(binary_string[:W],2)
        V = int(binary_string[W:],2)
        return U,V
    
    a = dao_mang(A)
    b = dao_mang(B)
    
    for i in range(0,t,1):
        U=0
        for j in range(0,t,1):
            C[i+j] = C[i+j] + a[i]*b[j] + U
            U,V = Chuyen_sang_UV(C[i+j],W)
            C[i+j] = V
        
        C[i+t] = U
        
    return dao_mang(C)


a = [0, 11, 173, 248]
b = [0, 1, 226, 64] 

x = phep_nhan_mang(a,b,4,8)
print(x)

     
    
    
    



    