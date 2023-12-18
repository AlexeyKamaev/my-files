from math import factorial as F

def C(n,m):
    return F(m)/(F(n)*F(m-n))



print(C(1,4))