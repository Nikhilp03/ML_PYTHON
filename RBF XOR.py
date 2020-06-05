#Auhtor: Nikhil .V. Pachkor
#RBF XOR Python
import numpy as np
import math
from numpy.linalg import inv
x=[[0,0],[0,1],[1,0],[1,1]]
d=np.array([0,1,1,0])
t1=np.array([1,1])
t2=np.array([0,0])
z1=[]
z2=[]
for i in range(4):
    y=np.subtract(np.array(x[i]),np.array(t1))
    se=0
    se+=( (y[0]**2)+(y[1]**2))
    se=np.sqrt(se)
    z1.append(math.exp(-(se**2)))
for i in range(4):
    y=np.subtract(np.array(x[i]),np.array(t2))
    se=0
    se+=( (y[0]**2)+(y[1]**2))
    se=np.sqrt(se)
    z2.append(math.exp(-(se**2)))
z=np.reshape([z1,z2],(2,4))
r=inv(np.mat(np.array(z))*np.mat(np.transpose(np.array(z))))
d=np.array(d)[np.newaxis]
d=d.T
t=np.mat(np.array(z))*np.mat(d)
u=np.mat(r)*np.mat(t)
z=np.array(z)[np.newaxis]
z=z.T
e=np.mat(np.array(z))*np.mat(np.array(u))
print(e)
