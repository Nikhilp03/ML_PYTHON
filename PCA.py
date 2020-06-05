#Author: Nikhil .V. Pachkor
#Principle Component analysis Python
from statistics import mean
import numpy as np
from matplotlib import pyplot as plt
x=[2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.2]
y=[2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9]
xmean=mean(x)
ymean=mean(y)
xsub=np.subtract(np.array(x),np.array([xmean]*len(x)))
ysub=np.subtract(np.array(y),np.array([xmean]*len(y)))
v=np.cov(x,y)
eig_vals, eig_vecs = np.linalg.eig(v)
for i in range(len(eig_vals)):
    if eig_vals[i]==max(eig_vals):
        a=i
        pc1=eig_vecs[a]
print('The Priciple component PC1 is {0} and the maximum eigen value is {1}'.format(eig_vecs[a],max(eig_vals)))
finaldata=[]
for i in range(len(xsub)):
    b=0
    b+=abs(pc1[0])*xsub[i]
    b+=abs(pc1[1])*ysub[i]
    finaldata.append(b)
print(finaldata)
plt.scatter(range(10),finaldata,s=100,c='r')
plt.xticks(np.arange(0, 10, 1))
plt.yticks(np.arange(-2, 3, 0.2))
plt.title('Principal Component Analysis')
plt.show()


