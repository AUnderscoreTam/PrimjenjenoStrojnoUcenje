from sklearn import datasets
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as mpl
from scipy.cluster.hierarchy import dendrogram, linkage 

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

def main():
    X = generate_data(22,1)
    kMarray = []
    kMeans = KMeans(3)
    kMeans.fit(X)
    mpl.figure(1)
    mpl.scatter(X[:,1],X[:,0],c=kMeans.labels_)
    #mpl.show()
    for i in range(1,21):
        kMeans = KMeans(i)
        kMeans.fit(X)
        kMarray.append(kMeans.inertia_)
    mpl.figure(2)
    mpl.plot(range(1,21),kMarray)
    #mpl.show()
    mpl.figure(3)
    X=linkage(X)
    dendrogram(X)
    mpl.show()

main()

#Kmeans nije dobar u detekciji simbola

