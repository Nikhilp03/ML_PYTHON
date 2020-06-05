#Author: Nikhil .V. Pachkor
#KSOFM Python
import numpy as np
w=np.array([[0.2,0.6,0.5,0.9],[0.8,0.4,0.7,0.3]])
x=np.array([[1,1,0,0],[0,0,0,1],[0,0,1,1],[1,0,0,0]])
alpha=0.5
for i in range(1000):
    for j in range(4):
        a=np.subtract(x[j],w[0])
        t=np.multiply(a,a)
        d1=sum(t)
        b=np.subtract(x[j],w[1])
        p=np.multiply(b,b)
        d2=sum(p)
        if d1<d2:
            w[0]=np.add(w[0],alpha*a)
        else:
            w[1]=np.add(w[1],alpha*b)
print(w)
