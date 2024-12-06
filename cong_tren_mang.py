import math
import ttcoban

#A=[157, 0, 173, 23]
#B=[169, 1, 0, 64]
#W=8
#F=2147483647
#t=4

def phep_cong_mang(A,B,W,t):
    epsilon = 0
    list = [0] * t
    for i in range(t-1,-1,-1):
        x = 2 **(W)
        list[i] = A[i]+B[i]+epsilon
        if (list[i]>=x):
            epsilon = 1
            list[i]=list[i]%x
        else:
            epsilon = 0
    return epsilon,list


#print(phep_cong_mang(A,B,W,t))


def phep_tru_mang(A,B,W,t):
    epsilon = 0;
    list = [0]*t
    for i in range(t-1,-1,-1):
        x = 2**(W)
        list[i] = A[i] - B[i] - epsilon
        if (list[i]<0):
            epsilon = 1
            list[i] = list[i] + x
        else:
            epsilon = 0
    return list,epsilon

#print(phep_tru_mang(A,B,W,t))    
    
    