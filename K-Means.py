#Author: Nikhil .V. Pachkor
#K-Means Clustering Python
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'x': [1,1.5,3,5,3.5,4.5,3.5],
    'y': [1,2,4,7,5,5,4.5]
})
c1=[1,1];
c2=[5,7];
k=2
centroids = {1:c1,2:c2}
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'],s=100,alpha=0.8, color='k') #print figure 1
colmap = {1: 'r', 2: 'g', 3: 'b'}
mapu={1: 'y', 2: 'y'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 6)
plt.ylim(0, 8)

def assignment(df, centroids):
    for i in centroids.keys():
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(df, centroids)
print(df.head(7)) # print table with distance last updated

fig = plt.figure(figsize=(7, 7))
plt.scatter(df['x'], df['y'], color=df['color'],s=100, alpha=0.8, edgecolor='k') #print figure 2
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 6)
plt.ylim(0, 8)


old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k

centroids = update(centroids)

fig = plt.figure(figsize=(7, 7))
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'],s=100, alpha=0.8, edgecolor='k') #print figure
for i in centroids.keys():
    plt.scatter(*centroids[i], s = 100, color=mapu[i])
plt.xlim(0, 6)
plt.ylim(0, 8)
plt.show()
for i in centroids:
    print('The Centroids of the clusters {0} is {1}'.format(i,centroids[i]))
