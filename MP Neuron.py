#Author: Nikhil .V. Pachkor
#MP Neuron Model
import operator
import numpy as np
data=[[0,0],[0,1],[1,0],[1,1]]
w=[1,1]
theta=0
s=''
while 1:
    x=int(input('Enter your Choice \n1.AND\n2.OR\n3.NOR\n4.NAND'))
    print(x)
    if x==0:
        break
    if x==1:
        w=[1,1]
        theta=2
        s='AND'
    if x==2:
        w=[1,1]
        theta=1
        s='OR'
    if x==3:
        w=[-1,-1]
        theta=0
        c=1
        s='NOR'
    if x==4:
        w=[-1,-1]
        theta=-1
        s='NAND'
    y=[]
    for i in range(len(data)):
        y.append( sum ( np.multiply ( np.array(data[i]),np.array(w) ) ) )
    print(y)
    print(s)

    for i in range(len(y)):
        if y[i]>=theta:
            y[i]=1
        else:
            y[i]=0

    for i in range(len(data)):
        print(*data[i],y[i])







